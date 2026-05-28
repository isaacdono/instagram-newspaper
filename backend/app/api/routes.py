from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.post import Post
from app.schemas.post import PostResponse

router = APIRouter()

@router.get("/feed", response_model=List[PostResponse])
def get_daily_feed(db: Session = Depends(get_db)):
    """
    Retorna os posts mais recentes do nosso banco de dados.
    """
    # Consulta: SELECT * FROM posts ORDER BY date DESC LIMIT 20
    posts = db.query(Post).order_by(Post.date.desc()).limit(20).all()
    return posts
