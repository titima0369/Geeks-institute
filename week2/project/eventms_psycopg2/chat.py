from flask import Blueprint, request, jsonify
from agent import ask_agent

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    question = (data.get("message") or "").strip()
    
    if not question:
        return jsonify({"answer": "Please send a message."}), 400

    answer = ask_agent(question)
    return jsonify({"answer": answer})
