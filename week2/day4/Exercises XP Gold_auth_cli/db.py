import sqlite3
from typing import Optional, Tuple

DB_PATH = "auth_cli.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL UNIQUE,
      password TEXT NOT NULL
    );
    """)
    conn.commit()
    conn.close()

def get_user(username: str) -> Optional[Tuple[int, str, str]]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username, password FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    return row

def create_user(username: str, hashed_password: str) -> bool:
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False
    except Exception:
        return False
