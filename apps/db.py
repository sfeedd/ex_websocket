# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/dbname"  # 데이터베이스 연결 URL

# SQLAlchemy 엔진
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 로컬
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 세션을 FastAPI에 연결
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
