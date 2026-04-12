from app.core.db import get_pool
from app.core.config import settings
from app.services.embedder import embed

async def retrieve(question: str, top_k: int | None = None) -> list[dict]:
  k = top_k or settings.retrieval_top_k
  query_embedding = embed(question)

  pool = await get_pool()
  async with pool.acquire() as conn:
    rows = await conn.fetch(
      """
      SELECT c.content, c.document_id, d.title, c.embedding <=> $1 AS distance
      FROM chunks c
      JOIN documents d ON d.id = c.document_id
      ORDER by distance
      LIMIT $2
      """,
      query_embedding, k
    )
  return [dict(row) for row in rows]
