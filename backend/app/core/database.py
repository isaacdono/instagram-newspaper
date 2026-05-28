from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do SQLite: o arquivo do banco se chamará "newspaper.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./newspaper.db"

# engine é a nossa ponte de comunicação com o banco de dados
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # Necessário apenas para o SQLite
)

# A Sessão é responsável por agrupar transações e enviá-las ao banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para criar os modelos de tabelas
Base = declarative_base()

# Dependência do FastAPI: Abre a conexão quando o usuário acessa uma rota, e fecha quando termina
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
