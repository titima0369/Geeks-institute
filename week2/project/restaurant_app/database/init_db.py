import psycopg2
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
result = urlparse(DATABASE_URL)

conn = psycopg2.connect(
    host=result.hostname,
    port=result.port or 5432,
    database=result.path[1:],
    user=result.username,
    password=result.password,
    sslmode="require"
)
cur = conn.cursor()

# تنفيذ جميع SQL من الملف
with open("index.sql", "r") as f:
    cur.execute(f.read())

conn.commit()
cur.close()
conn.close()

print("Database tables created successfully!")
