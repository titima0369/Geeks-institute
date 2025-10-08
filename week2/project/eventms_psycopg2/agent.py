# agent.py
from dotenv import load_dotenv
import os, json
import psycopg2
from openai import OpenAI, RateLimitError, APIConnectionError, AuthenticationError, APIError
from datetime import datetime

load_dotenv()

# ----------------- OpenAI Setup -----------------
api_key = os.getenv("GIT_API_KEY")
if not api_key:
    raise RuntimeError("GIT_API_KEY is missing from your environment/.env")

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
client = OpenAI(api_key=api_key, base_url=endpoint)

SYSTEM_PROMPT = "أنت مساعد ذكي لموقع Event Management."

# ----------------- Database Setup -----------------
DB_URL = os.getenv("DATABASE_URL")
FALLBACK_FILE = "unanswered_queries.json"

def get_conn(sql, params=None):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute(sql, params or ())
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# ----------------- JSON Fallback -----------------
def load_fallback_data():
    if os.path.exists(FALLBACK_FILE):
        try:
            with open(FALLBACK_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {"queries": [], "responses": {}}
    return {"queries": [], "responses": {}}

def save_fallback_data(data):
    with open(FALLBACK_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_unanswered_query(question, ai_response):
    fallback_data = load_fallback_data()
    query_entry = {
        "id": len(fallback_data["queries"]) + 1,
        "question": question,
        "timestamp": datetime.now().isoformat(),
        "ai_response": ai_response,
        "status": "pending"
    }
    fallback_data["queries"].append(query_entry)
    query_key = question.lower().strip()
    fallback_data["responses"][query_key] = ai_response
    save_fallback_data(fallback_data)
    return query_entry["id"]

def search_fallback_responses(question):
    fallback_data = load_fallback_data()
    query_key = question.lower().strip()
    if query_key in fallback_data["responses"]:
        return fallback_data["responses"][query_key]
    for stored_question, response in fallback_data["responses"].items():
        if any(word in stored_question for word in query_key.split() if len(word) > 3):
            return response
    return None

# ----------------- Structured Queries -----------------
def get_events_structured(start=None, end=None, limit=5):
    try:
        if start and end:
            rows = get_conn(
                "SELECT name, date, location FROM events WHERE date BETWEEN %s AND %s ORDER BY date",
                (start, end)
            )
        else:
            rows = get_conn(
                "SELECT name, date, location FROM events ORDER BY date LIMIT %s",
                (limit,)
            )
        return [dict(name=r[0], date=str(r[1]), location=r[2]) for r in rows] if rows else []
    except Exception as e:
        print(f"Database error in get_events_structured: {e}")
        return []

def get_organizers_structured(limit=5):
    try:
        rows = get_conn("SELECT name, contact_info FROM organizers LIMIT %s", (limit,))
        return [dict(name=r[0], contact_info=r[1]) for r in rows] if rows else []
    except Exception as e:
        print(f"Database error in get_organizers_structured: {e}")
        return []

def get_attendees_structured(limit=5):
    try:
        rows = get_conn("SELECT name, email FROM attendees LIMIT %s", (limit,))
        return [dict(name=r[0], email=r[1]) for r in rows] if rows else []
    except Exception as e:
        print(f"Database error in get_attendees_structured: {e}")
        return []

def get_tickets_structured(limit=5):
    try:
        rows = get_conn("SELECT type, price FROM tickets LIMIT %s", (limit,))
        return [dict(type=r[0], price=r[1]) for r in rows] if rows else []
    except Exception as e:
        print(f"Database error in get_tickets_structured: {e}")
        return []

def search_general_info(query):
    try:
        events = get_conn(
            "SELECT name, date, location, description FROM events WHERE name ILIKE %s OR description ILIKE %s LIMIT 3",
            (f"%{query}%", f"%{query}%")
        )
        organizers = get_conn(
            "SELECT name, contact_info FROM organizers WHERE name ILIKE %s LIMIT 2",
            (f"%{query}%",)
        )
        results = {
            "events": [dict(name=r[0], date=str(r[1]), location=r[2], description=r[3] if len(r) > 3 else "") for r in events],
            "organizers": [dict(name=r[0], contact_info=r[1]) for r in organizers]
        }
        return results if (results["events"] or results["organizers"]) else None
    except Exception as e:
        print(f"Database error in search_general_info: {e}")
        return None

# ----------------- Tools -----------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_events_structured",
            "description": "Fetch upcoming events from database",
            "parameters": {
                "type": "object",
                "properties": {
                    "start": {"type": "string", "format": "date"},
                    "end": {"type": "string", "format": "date"},
                    "limit": {"type": "integer"}
                },
                "required": ["limit"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_organizers_structured",
            "description": "Fetch list of organizers",
            "parameters": {
                "type": "object",
                "properties": {"limit": {"type": "integer"}},
                "required": ["limit"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_attendees_structured",
            "description": "Fetch list of attendees",
            "parameters": {
                "type": "object",
                "properties": {"limit": {"type": "integer"}},
                "required": ["limit"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_tickets_structured",
            "description": "Fetch available tickets",
            "parameters": {
                "type": "object",
                "properties": {"limit": {"type": "integer"}},
                "required": ["limit"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_general_info",
            "description": "Search for general information in the database",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"]
            }
        }
    }
]

# ----------------- Memory (in-memory list) -----------------
conversation_history = []

# ----------------- Agent Logic -----------------
def ask_agent(question: str) -> str:
    global conversation_history
    try:
        # Add user message to history
        conversation_history.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history,
            tools=tools,
            tool_choice="auto"
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            # Handle tool call same as before
            tool_call = msg.tool_calls[0]
            fn_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            match fn_name:
                case "get_events_structured":
                    result = get_events_structured(**args)
                case "get_organizers_structured":
                    result = get_organizers_structured(**args)
                case "get_attendees_structured":
                    result = get_attendees_structured(**args)
                case "get_tickets_structured":
                    result = get_tickets_structured(**args)
                case "search_general_info":
                    result = search_general_info(**args)
                case _:
                    result = {"error": "Unknown tool"}

            followup = client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] +
                         conversation_history +
                         [
                             msg,
                             {"role": "tool", "tool_call_id": tool_call.id,
                              "content": json.dumps(result, ensure_ascii=False)}
                         ]
            )
            final_response = followup.choices[0].message.content
        else:
            # Direct response
            final_response = msg.content

        # Save assistant reply to history
        conversation_history.append({"role": "assistant", "content": final_response})

        return final_response

    except (RateLimitError, APIConnectionError, AuthenticationError, APIError) as e:
        error_msg = f"❌ Error: {str(e)}"
        save_unanswered_query(question, error_msg)
        return error_msg

# ----------------- Utilities -----------------
def get_unanswered_queries():
    fallback_data = load_fallback_data()
    return fallback_data["queries"]

def update_query_status(query_id, status):
    fallback_data = load_fallback_data()
    for query in fallback_data["queries"]:
        if query["id"] == query_id:
            query["status"] = status
            break
    save_fallback_data(fallback_data)

def add_manual_response(question, response):
    fallback_data = load_fallback_data()
    query_key = question.lower().strip()
    fallback_data["responses"][query_key] = response
    save_fallback_data(fallback_data)

# ----------------- Example Usage -----------------
if __name__ == "__main__":
    test_questions = [
        "ما هي الأحداث القادمة؟",
        "تذكر أن اسمي هو إبراهيم",
        "من هم المنظمون؟",
        "ما هو اسمي؟"
    ]

    for q in test_questions:
        print(f"\nسؤال: {q}")
        answer = ask_agent(q)
        print(f"جواب: {answer}")
        print("-" * 50)
