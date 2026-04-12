from fastapi import APIRouter, Security
from app.core.auth import verify_api_key
from app.schemas.query import QueryRequest, QueryResponse
from app.services.retriever import retrieve
from app.services.generator import generate

router = APIRouter()

@router.post("/", response_model=QueryResponse)
async def query(
  request: QueryRequest,
  _=Security(verify_api_key)
):
  chunks = await retrieve(request.question, request.top_k)
  sources = list({chunk["title"] for chunk in chunks})
  answer = await generate(request.question, chunks)
  return QueryResponse(answer=answer, sources=sources)
