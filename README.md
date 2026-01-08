<div align="center">
# 🚀🚀🚀 Nano  - Simple & Fast Knowledge Graph RAG Solution

# local environment setup

1.

- install bash
- install docker (or podman)
- install vscode ( devaamiseen )


2.

mkdir nano
start bash

git clone https://github.com/markoviksten/nano2.git
cd nano2

mkdir -p data/nano{1..5}/{rag_storage,inputs}
mkdir -p agent/data/agent{1..5}
touch config.ini

cp env.example .env

EDIT .env : add following to there (copy-paste / huom openai api key tarvitaan! rerank jina apikey free käytössä)

AUTH_ACCOUNTS=admin:zadmin123,user1:zpass456
WORKERS=3
WORKER_TIMEOUT=180
TIMEOUT=180
EMBEDDING_BATCH_NUM=20 # oli 10 
EMBEDDING_BINDING=openai
EMBEDDING_BINDING_API_KEY=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
EMBEDDING_BINDING_HOST=https://api.openai.com/v1
EMBEDDING_DIM=1536
EMBEDDING_FUNC_MAX_ASYNC=3    #oli 24, kokeile myös 5
EMBEDDING_MODEL=text-embedding-3-small
EMBEDDING_FUNC_TIMEOUT=300
MAX_ASYNC_WORKERS=3
LIGHTRAG_API_KEY=your-secure-api-key-here-marko
LLM_BINDING=openai
LLM_BINDING_API_KEY=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
LLM_BINDING_HOST=https://api.openai.com/v1
LLM_MODEL=gpt-4.1-nano
MAX_ASYNC=6   #oli 12 
MAX_PARALLEL_INSERT=3
RERANK_BINDING_API_KEY=jina_e1691f3b27ee422b993677dfd10ce05dw7hpx78yohm2o5Jn1dQVjn5DBuTy
RERANK_BINDING_HOST=https://api.jina.ai/v1/rerank
RERANK_MODEL=jina-reranker-v2-base-multilingual
SUMMARY_LANGUAGE=English
EVAL_LLM_MAX_RETRIES=5
EVAL_LLM_TIMEOUT=180
VDB_TIMEOUT=240
VDB_MAX_RETRIES=5
MAX_CONCURRENT_EMBEDS=5
VECTOR_CHUNK_SIZE=500
VECTOR_CHUNK_OVERLAP=50
OPENAI_TIMEOUT=120
OPENAI_MAX_RETRIES=5


(muista käynnistää podman koneellasi: sitten aja asennus)
docker compose up -d

DONE!!

Verify that url respond now : 
Nano Agent http://localhost:9001/docs#/ - http://localhost:9005/docs#/
LightRAG http://localhost:9621/webui/ - http://localhost:9625/webui/
App UI  http://localhost:3000/

//// aftercare config - configuration guide : later-on finalized
webui webhook: https://169.51.48.29:5678/webhook/08149cd3-53bc-449b-a8ec-a54a2e68b770
put testiyhteys.json to n8n to serve this / reconfigure points corectly

CLOSE SYSTEM
docker compose down

huom asenna paikallinen n8n / ohessa esimerkki komento
podman run -it --rm   --name n8n   -p 5678:5678   -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true   -e N8N_RUNNERS_ENABLED=true   -e N8N_HOST=127.0.0.1   -e N8N_PORT=5678   -e N8N_PROTOCOL=http   -e N8N_COMMUNITY_PACKAGES_ENABLED=true   -v n8n_data:/home/node/.n8n   -v "C:\Users\861100702\Documents\n8n\n8n_data":/home/node/excel   --dns=8.8.8.8   --dns=8.8.4.4   docker.n8n.io/n8nio/n8n start

keycloak asennus & konffaus identiteetinhallintaan UI:ta varten?

# cloud environment setup

Saman tyyppinen set up cloudiin paitsi tilaat ensin IBM Cloud tililtä koneen mihin kaikke asennetaan,

1. Cloud Machine setup

2. Nano asennus cloudissa

loggaa sisään cloudi koneeseen
ssh@iposoite.ocm
yes
salasana


huom asenna cloud n8n / ohessa esimerkki komento (huomaa tarttet ip osoiteen isäntäkoneelta ensin)
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  -e N8N_RUNNERS_ENABLED=true \
  -e N8N_COMMUNITY_PACKAGES_ENABLED=true \
  -e N8N_HOST=169.51.48.29 \
  -e N8N_PORT=5678 \
  -e N8N_PROTOCOL=https \
  -e N8N_EDITOR_BASE_URL=https://169.51.48.29:5678 \
  -e WEBHOOK_URL=https://169.51.48.29:5678 \
  -e N8N_SSL_KEY=/certs/private.key \
  -e N8N_SSL_CERT=/certs/certificate.crt \
  -v n8n_data:/home/node/.n8n \
  -v ~/n8n/n8n_data:/home/node/excel \
  -v ~/n8n/certs:/certs \
  --dns=8.8.8.8 \
  --dns=8.8.4.4 \
  docker.n8n.io/n8nio/n8n start
