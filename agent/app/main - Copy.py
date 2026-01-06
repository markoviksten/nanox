from fastapi import FastAPI, Request
import requests, json, logging
from app.db import init_db, log_query, get_recent_queries, get_query_detail

logging.basicConfig(level=logging.INFO)
app = FastAPI()
LIGHTRAG_URL = "http://lightrag:9621/query"

@app.on_event("startup")
def startup():
    init_db()
    logging.info("SQLite DB initialized")

@app.post("/query")
async def query(req: Request):
    body = await req.json()
    question = body.get("question")
    user_id = body.get("user_id", "anonymous")
    logging.info(f"{user_id}: {question}")

    r = requests.post(LIGHTRAG_URL, json={"query": question}, timeout=60)
    response_json = r.json()

    log_query(user_id, question, json.dumps(response_json))
    return {"query": question, "answer": response_json}

@app.get("/dashboard/queries")
def dashboard_queries(limit: int = 50):
    return get_recent_queries(limit)

@app.get("/dashboard/query/{query_id}")
def dashboard_query(query_id: int):
    return get_query_detail(query_id)
