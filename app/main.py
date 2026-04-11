from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import create_pool, close_pool
from app.api.routes import health, ingest, query

@asynccontextmanager
async def lifespan(app: FastAPI):
  await create_pool()
  yield
  await close_pool()

app = FastAPI(title = "RAG Risk Analysis Service", lifespan = lifespan)

app.include_router(health.router)
app.include_router(ingest.router, prefix = "/ingest")
app.include_router(query.router, prefix = "/query")
