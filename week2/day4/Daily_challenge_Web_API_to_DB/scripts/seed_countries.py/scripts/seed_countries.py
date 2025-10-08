
import os
import random
import sys
import requests
import psycopg2
from psycopg2.extras import execute_values

API_URL = "https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population"

DB_NAME = os.getenv("PGDATABASE", "Restaurant_Menu")
DB_USER = os.getenv("PGUSER", "postgres")
DB_PASSWORD = os.getenv("PGPASSWORD", "root")
DB_HOST = os.getenv("PGHOST", "localhost")
DB_PORT = os.getenv("PGPORT", "5432")


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
            host=DB_HOST, port=DB_PORT
        )
        conn.autocommit = True
        return conn
    except Exception as e:
        print(f"DB connection failed: {e}")
        sys.exit(1)


def fetch_all_countries():
    try:
        resp = requests.get(API_URL, timeout=20)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Failed to fetch API: {e}")
        sys.exit(1)


def normalize_country(raw):
    name = None
    if isinstance(raw.get("name"), dict):
        name = raw["name"].get("common") or raw["name"].get("official")
    else:
        name = str(raw.get("name"))

    capital_raw = raw.get("capital")
    if isinstance(capital_raw, list):
        capital = ", ".join([str(c) for c in capital_raw])
    elif capital_raw is None:
        capital = None
    else:
        capital = str(capital_raw)

    flag = raw.get("flag")
    subregion = raw.get("subregion")
    population = raw.get("population") or 0

    return (name, capital, flag, subregion, int(population))


def ensure_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS countries (
          id SERIAL PRIMARY KEY,
          name TEXT NOT NULL UNIQUE,
          capital TEXT,
          flag TEXT,
          subregion TEXT,
          population BIGINT NOT NULL DEFAULT 0
        );
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_countries_subregion ON countries(subregion);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_countries_population ON countries(population);")


def insert_countries(conn, countries_rows):
    query = """
    INSERT INTO countries (name, capital, flag, subregion, population)
    VALUES %s
    ON CONFLICT (name) DO UPDATE
      SET capital = EXCLUDED.capital,
          flag = EXCLUDED.flag,
          subregion = EXCLUDED.subregion,
          population = EXCLUDED.population;
    """
    with conn.cursor() as cur:
        execute_values(cur, query, countries_rows)
        touched = cur.rowcount
    return touched


def main():
    print("Fetching countries ...")
    all_countries = fetch_all_countries()
    if not all_countries:
        print("API returned empty list.")
        sys.exit(1)

    k = min(10, len(all_countries))
    sample = random.sample(all_countries, k)
    rows = [normalize_country(c) for c in sample if c]
    rows = [r for r in rows if r[0]]

    conn = get_connection()
    ensure_table(conn)

    print(f"Inserting/Updating {len(rows)} countries ...")
    touched = insert_countries(conn, rows)

    with conn.cursor() as cur:
        cur.execute(
            "SELECT name, capital, flag, subregion, population FROM countries WHERE name = ANY(%s) ORDER BY name ASC",
            ([r[0] for r in rows],)
        )
        preview = cur.fetchall()

    print(f"Done. Rows touched (inserted or updated): {touched}")
    print("—— Preview ——")
    for (name, capital, flag, subregion, population) in preview[:10]:
        print(f"- {name} ({flag}) — Capital: {capital or '—'}, Subregion: {subregion or '—'}, Pop: {population:,}")

    conn.close()


if __name__ == "__main__":
    main()
