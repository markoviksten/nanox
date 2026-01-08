from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import requests
import os

app = FastAPI(
    title="Nano Agent API",
    version="0.2.0"
)

# ---------
# CORS (KORJAUS OPTIONS 405 -ONGELMAAN)
# ---------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # kehityksessä ok, rajaa prodissa
    allow_credentials=True,
    allow_methods=["*"],        # POST, OPTIONS, GET, jne
    allow_headers=["*"],
)

# ---------
# Request / Response -mallit
# ---------
class Reference(BaseModel):
    reference_id: str
    file_path: str
    content: Optional[str] = None

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    question: str
    timestamp: str
    status: str
    text: str
    references: Optional[List[Reference]] = []

# ---------
# In-memory log (korvataan myöhemmin SQLitellä)
# ---------
QUERY_LOG: List[QueryResponse] = []

# ---------
# LightRAG URL + auth (ympäristömuuttujat)
# ---------
LIGHTRAG_URL = os.getenv("LIGHTRAG_URL", "http://lightrag:9621/query")
API_KEY = os.getenv("API_KEY", "")
BEARER_TOKEN = os.getenv("BEARER_TOKEN", "")

LIGHTRAG_HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "X-API-Key": API_KEY,
    "Content-Type": "application/json",
    "accept": "application/json"
}

# ---------
# Endpoints
# ---------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    try:
        resp = requests.post(
            LIGHTRAG_URL,
            json={"query": req.question},
            headers=LIGHTRAG_HEADERS,
            timeout=60.0
        )
        resp.raise_for_status()
        resp_json = resp.json()

        rag_text = resp_json.get("response", "No answer")

        rag_references = [
            Reference(
                reference_id=ref.get("reference_id", ""),
                file_path=ref.get("file_path", ""),
                content=ref.get("content")
            )
            for ref in resp_json.get("references", [])
        ]

        status = "answered"

    except Exception as e:
        rag_text = f"Error: {e}"
        rag_references = []
        status = "failed"

    entry = QueryResponse(
        question=req.question,
        timestamp=datetime.utcnow().isoformat(),
        status=status,
        text=rag_text,
        references=rag_references
    )

    QUERY_LOG.append(entry)
    return entry

@app.get("/dashboard/queries", response_model=List[QueryResponse])
def dashboard_queries():
    return QUERY_LOG
