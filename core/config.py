from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file=".env", extra="ignore")

  #database
  database_url: str

  #auth
  api_key: str

  #embedder
  embedding_model: str = "all-MiniLM-L6-v2"
  embedding_dim: int = 384

  #claude
  anthropic_api_key: str
  claude_model: str = "claude-sonnet-4-6"

  #retrieval
  retrieval_top_k: int = 5

settings = Settings()