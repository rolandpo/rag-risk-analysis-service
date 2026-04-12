import anthropic
from app.core.config import settings

_client: anthropic.Anthropic | None = None

def get_client() -> anthropic.Anthropic:
  global _client
  if _client is None:
    _client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
  return _client

async def generate(question: str, chunks: list[dict]) -> str:
  context = "\n\n".join(
    f"[{i+1}] {chunk['title']}: {chunk['content']}"
    for i, chunk in enumerate(chunks)
  )

  prompt = f"""You are a risk analysis assistant. Answer the question using only the context provided.

  Context: {context}

  Question: {question}

  Answer:"""

  client = get_client()
  message = client.messages.create(
    model=settings.claude_model,
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}]
  )

  return message.content[0].text
