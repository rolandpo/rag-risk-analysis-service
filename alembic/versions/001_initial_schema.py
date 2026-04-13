from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

revision = "001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
  op.execute("CREATE EXTENSION IF NOT EXISTS vector")
  op.create_table(
    "documents",
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("title", sa.String, nullable=False),
    sa.Column("metadata", sa.JSON, nullable=False, server_default="{}"),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now())
  )

  op.create_table(
    "chunks",
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("document_id", sa.String, sa.ForeignKey("documents.id"), nullable=False),
    sa.Column("content", sa.Text, nullable=False),
    sa.Column("embedding", Vector(384), nullable=False),
    sa.Column("chunk_index", sa.Integer, nullable=False)
  )

  op.create_index(
    "chunks_embedding_idx",
    "chunks",
    ["embedding"],
    postgresql_using="ivfflat",
    postgresql_with={"lists": 100},
    postgresql_ops={"embedding": "vector_cosine_ops"}
  )

def downgrade() -> None:
  op.drop_index("chunks_embedding_idx")
  op.drop_table("chunks")
  op.drop_table("documents")
