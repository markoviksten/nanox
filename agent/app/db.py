import sqlite3
from datetime import datetime

DB_PATH = "/data/agent.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # Päätaulu queries
    cur.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_id TEXT,
            agent_id TEXT,
            question TEXT,
            text TEXT
        )
    """)

    # Viitteet
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

def log_query(user_id, question, text, agent_id=None, references=None):
    """
    agent_id: esim. nano-1, nano-2 ...
    references: lista dict objekteja
    """
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO queries (timestamp, user_id, agent_id, question, text)
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.utcnow().isoformat(),
        user_id,
        agent_id,
        question,
        text
    ))
    query_id = cur.lastrowid

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

def get_recent_queries(limit=50, agent_id=None):
    conn = get_conn()
    cur = conn.cursor()

    if agent_id:
        cur.execute("""
            SELECT id, timestamp, user_id, agent_id, question
            FROM queries
            WHERE agent_id = ?
            ORDER BY id DESC
            LIMIT ?
        """, (agent_id, limit))
    else:
        cur.execute("""
            SELECT id, timestamp, user_id, agent_id, question
            FROM queries
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "timestamp": r[1],
            "user_id": r[2],
            "agent_id": r[3],
            "question": r[4],
        }
        for r in rows
    ]

def get_query_detail(query_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT timestamp, user_id, agent_id, question, text
        FROM queries
        WHERE id = ?
    """, (query_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        return None

    query_data = {
        "timestamp": row[0],
        "user_id": row[1],
        "agent_id": row[2],
        "question": row[3],
        "text": row[4],
        "references": []
    }

    cur.execute("""
        SELECT reference_id, file_path, content
        FROM references
        WHERE query_id = ?
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
