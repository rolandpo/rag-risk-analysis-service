import asyncpg
from app.core.config import settings

_pool: asyncpg.Pool | None = None

async def create_pool() -> None:
  global _pool
  _pool = await asyncpg.create_pool(settings.database_url)

async def close_pool() -> None:
  if _pool:
    await _pool.close()

async def get_pool() -> asyncpg.Pool:
  if _pool is None:
    raise RuntimeError("Database pool not initialized")
  return _pool
