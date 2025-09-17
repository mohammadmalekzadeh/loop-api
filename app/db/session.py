# app/database/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL, TEST_DB_URL

# engine = create_engine(DATABASE_URL, echo=True)
engine = create_engine(TEST_DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
