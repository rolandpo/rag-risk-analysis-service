fastapi
uvicorn
sqlalchemy
psycopg2-binary
pgvector
pydantic
python-dotenv
openai
pytest


uv init rag-risk-service
cd rag-risk-service
uv add fastapi uvicorn sqlalchemy psycopg2-binary

app/
  main.py
  config.py
  api/
  services/
  db/
tests/

rag-risk-analysis-service/                                             
  ├── app/                                                               
  │   ├── __init__.py                                                    
  │   ├── main.py                  # FastAPI app + lifespan              
  │   ├── api/                                                           
  │   │   └── routes/                                                    
  │   │       ├── health.py              
  │   │       ├── ingest.py        # POST /ingest                        
  │   │       └── query.py         # POST /query
  │   ├── core/                                                          
  │   │   ├── config.py            # settings via pydantic-settings
  │   │   ├── db.py                # asyncpg connection pool             
  │   │   └── auth.py              # API key header validation           
  │   ├── schemas/                 
  │   │   ├── ingest.py            # request/response models             
  │   │   └── query.py                                                   
  │   └── services/                
  │       ├── embedder.py          # sentence-transformers               
  │       ├── ingester.py          # chunking + storing docs             
  │       ├── retriever.py         # vector similarity search
  │       └── generator.py        # Claude API call                      
  ├── alembic/                                                           
  │   ├── env.py                                                         
  │   ├── script.py.mako                                                 
  │   └── versions/                                                      
  │       └── 001_initial_schema.py   # documents + chunks tables
  ├── tests/                                                             
  │   ├── conftest.py                    
  │   ├── test_ingest.py
  │   └── test_query.py                                                  
  ├── docker/                            
  │   └── Dockerfile                                                     
  ├── .github/                           
  │   └── workflows/                                                     
  │       └── ci.yml               # lint + test
  ├── docker-compose.yml           # app + postgres/pgvector             
  ├── pyproject.toml                     
  ├── alembic.ini                  
  └── .env.example