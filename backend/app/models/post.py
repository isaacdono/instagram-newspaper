from sqlalchemy import Column, Integer, String, DateTime, Text
from app.core.database import Base
from datetime import datetime

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    shortcode = Column(String, unique=True, index=True) # ID único do post no instagram
    author = Column(String, index=True)
    caption = Column(Text, nullable=True) # A legenda completa
    image_url = Column(String) # O caminho local arquivo: /static/feed/xxx.jpg
    date = Column(DateTime, default=datetime.utcnow) # Data original do post
    category = Column(String, default="LATEST") # Para usarmos no site (News, Culture, etc)
