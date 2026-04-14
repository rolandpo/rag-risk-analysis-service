rag risk analysis service

uv init rag-risk-service
cd rag-risk-service
uv add fastapi uvicorn sqlalchemy psycopg2-binary

docker compose up --build

docker compose run app uv run alembic upgrade head
curl http://localhost:8000/health
uv run pytest tests/

ingest

curl -X POST http://localhost:8000/ingest/ -H "Content-Type: application/json" -H "X-API-Key: key-1234" -d '{"title": "Risk Report Q1", "content": "Market risk increased significantly in Q1 2024 due to rising interest rates and geopolitical tensions. Credit exposure remained within acceptable limits."}'

query                                                                                
curl -X POST http://localhost:8000/query/ -H "Content-Type: application/json" -H "X-API-Key: key-1234" -d '{"question": "What happened to market risk in Q1?"}'
