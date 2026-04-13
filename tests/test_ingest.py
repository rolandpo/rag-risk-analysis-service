import pytest
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_ingest_success(client):
  with patch("app.api.routes.ingest.ingest_document", new_callable=AsyncMock) as mock:
    mock.return_value = ("doc-123", 5)
    response = await client.post(
      "/ingest/",
      json={"title": "Test Doc", "content": "Some risk content"},
      headers={"X-API-Key": "key-1234"}
    )
  assert response.status_code == 200
  assert response.json()["document_id"] == "doc-123"
  assert response.json()["chunk_count"] == 5

@pytest.mark.asyncio
async def test_ingest_unauthorized(client):
  response = await client.post(
    "/ingest/",
    json={"title": "Test Doc", "content": "Some content"}
  )
  assert response.status_code == 401
