from pydantic import BaseModel

class IngestRequest(BaseModel):
  title: str
  content: str
  metadata: dict = {}

class IngestResponse(BaseModel):
  document_id: str
  chunk_count: int
