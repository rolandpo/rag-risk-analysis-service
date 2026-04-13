import pytest
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_query_success(client):
  with patch("app.api.routes.query.retrieve", new_callable=AsyncMock) as mock_retrieve, patch("app.api.routes.query.generate", new_callable=AsyncMock) as mock_generate:
    mock_retrieve.return_value = [{"title": "Risk Report", "content": "..."}]
    mock_generate.return_value = "The risk is low."
    response = await client.post(
      "/query/",
      json={"question": "What is the risk?"},
      headers={"X-API-Key": "key-1234"}
    )
  assert response.status_code == 200
  assert response.json()["answer"] == "The risk is low."

@pytest.mark.asyncio
async def test_query_unauthorized(client):
  response = await client.post(
    "/query/",
    json={"question": "What is the risk?"}
  )
  assert response.status_code == 401
