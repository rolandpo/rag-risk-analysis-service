rag risk analysis service

**ingest**
curl -X POST http://localhost:8000/ingest/ -H "Content-Type: application/json" -H "X-API-Key: key-1234" -d '{"title": "Risk Report Q1", "content": "Market risk increased significantly in Q1 2024 due to rising interest rates and geopolitical tensions. Credit exposure remained within acceptable limits."}'

**query**
curl -X POST http://localhost:8000/query/ -H "Content-Type: application/json" -H "X-API-Key: key-1234" -d '{"question": "What happened to market risk in Q1?"}'

docker compose up --build app

docker compose exec app uv run alembic upgrade head
curl http://localhost:8000/health
uv run pytest tests/
**ingest**
docker compose exec db psql -U postgres -d rag_risk -c "SELECT id, title FROM documents;"
docker compose exec db psql -U postgres -d rag_risk -c "\dt"
**query**
