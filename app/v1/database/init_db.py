# app/database/init_db.py

from app.v1.database.base import Base
from app.v1.database.session import engine

def init_db():
    Base.metadata.create_all(bind=engine)