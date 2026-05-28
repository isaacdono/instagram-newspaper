from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes

from app.core.database import engine, Base
import app.models.post # Garantir que o SQLAlchemy localize as tabelas antes de criar

# Cria o arquivo newspaper.db e todas as tabelas caso não existam
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Instagram Newspaper API")

# Allow frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, change to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the downloaded images statically
# the frontend can access images like: http://localhost:8000/static/feed/post_shortcode.jpg
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include our API routes
app.include_router(routes.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Feed Chronicle API!"}
