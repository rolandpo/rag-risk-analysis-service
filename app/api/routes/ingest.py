from fastapi import APIRouter, Security
from app.core.auth import verify_api_key
from app.schemas.ingest import IngestRequest, IngestResponse
from app.services.ingester import ingest_document

router = APIRouter()

@router.post("/", response_model=IngestResponse)
async def ingest(
  request: IngestRequest,
  _=Security(verify_api_key)
):
  document_id, chunk_count = await ingest_document(
    title=request.title,
    content=request.content,
    metadata=request.metadata
  )
  return IngestResponse(docuemnt_id=document_id, chunk_count=chunk_count)
