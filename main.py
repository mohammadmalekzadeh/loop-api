# app/main.py

from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.v1.endpoints.auth import auth

app = FastAPI()

app.include_router(auth.router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get('/')
def read_root():
    return {'Hello': 'World'}