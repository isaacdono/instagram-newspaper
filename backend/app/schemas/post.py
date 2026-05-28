from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema base
class PostBase(BaseModel):
    shortcode: str
    author: str
    caption: Optional[str] = None
    image_url: str
    date: datetime
    category: str

# Schema usado para CADASTRAR post no banco (futuro)
class PostCreate(PostBase):
    pass

# Schema de RESPOSTA do servidor (o que o frontend vai receber)
class PostResponse(PostBase):
    id: int

    class Config:
        from_attributes = True # Avisa o Pydantic que ele está lidando com modelos SQLAlchemy
