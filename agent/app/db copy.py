import sqlite3
from datetime import datetime
import json

DB_PATH = "/data/agent.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # Päätaulu queries (response → text)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_id TEXT,
            question TEXT,
            text TEXT
        )
    """)

    # Viitteet taulu
    cur.execute("""
        CREATE TABLE IF NOT EXISTS references (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_id INTEGER,
            reference_id TEXT,
            file_path TEXT,
            content TEXT,
            FOREIGN KEY (query_id) REFERENCES queries(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()

def log_query(user_id, question, text, references=None):
    """
    references: lista dict objekteja [{"reference_id":..., "file_path":..., "content":...}, ...]
    """
    conn = get_conn()
    cur = conn.cursor()

    # Lisää pääkysely
    cur.execute("""
        INSERT INTO queries (timestamp, user_id, question, text)
        VALUES (?, ?, ?, ?)
    """, (datetime.utcnow().isoformat(), user_id, question, text))
    query_id = cur.lastrowid

    # Lisää viitteet, jos niitä on
    if references:
        for ref in references:
            cur.execute("""
                INSERT INTO references (query_id, reference_id, file_path, content)
                VALUES (?, ?, ?, ?)
            """, (
                query_id,
                ref.get("reference_id", ""),
                ref.get("file_path", ""),
                ref.get("content")
            ))

    conn.commit()
    conn.close()

def get_recent_queries(limit=50):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, timestamp, user_id, question
        FROM queries
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "timestamp": r[1], "user_id": r[2], "question": r[3]} for r in rows]

def get_query_detail(query_id):
    conn = get_conn()
    cur = conn.cursor()

    # Hae pääkysely
    cur.execute("""
        SELECT timestamp, user_id, question, text
        FROM queries WHERE id = ?
    """, (query_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        return None

    query_data = {
        "timestamp": row[0],
        "user_id": row[1],
        "question": row[2],
        "text": row[3],
        "references": []
    }

    # Hae viitteet
    cur.execute("""
        SELECT reference_id, file_path, content
        FROM references WHERE query_id = ?
    """, (query_id,))
    ref_rows = cur.fetchall()
    for r in ref_rows:
        query_data["references"].append({
            "reference_id": r[0],
            "file_path": r[1],
            "content": r[2]
        })

    conn.close()
    return query_data
