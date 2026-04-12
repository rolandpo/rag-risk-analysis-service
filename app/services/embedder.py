from sentence_transformers import SentenceTransformer
from app.core.config import settings

_model: SentenceTransformer | None = None

def get_model() -> SentenceTransformer:
  global _model
  if _model is None:
    _model = SentenceTransformer(settings.embedding_model)
  return _model

def embed(text: str) -> list[float]:
  model = get_model()
  return model.encode(text).tolist()

def embed_many(texts: list[str]) -> list[list[float]]:
  model = get_model()
  return model.encode(texts).tolist()
