import uuid
import json
from app.core.db import get_pool
from app.services.embedder import embed_many

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def chunk_text(text: str) -> list[str]:
  chunks = []
  start = 0
  while start < len(text):
    end = start + CHUNK_SIZE
    chunks.append(text[start:end])
    start += CHUNK_SIZE - CHUNK_OVERLAP
  return chunks

async def ingest_document(title: str, content: str, metadata: dict) -> tuple[str, int]:
  document_id = str(uuid.uuid4())
  chunks = chunk_text(content)
  embeddings = embed_many(chunks)

  pool = await get_pool()
  async with pool.acquire() as conn:
    await conn.execute(
      "INSERT INTO documents (id, title, metadata) VALUES ($1, $2, $3)",
      document_id, title, json.dumps(metadata)
    )
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
      await conn.execute(
        "INSERT INTO chunks (id, document_id, content, embedding, chunk_index) VALUES ($1, $2, $3, $4, $5)",
        str(uuid.uuid4()), document_id, chunk, "[" + ",".join(map(str, embedding)) + "]", i
      )
  return document_id, len(chunks)
