# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.init_db import init_db
from app.api.v1.endpoints.auth import auth
from app.api.v1.endpoints.user import router as user
from app.api.v1.endpoints.request import request

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://loop-ui-nu.vercel.app"
]

app.include_router(auth.router)
app.include_router(user)
app.include_router(request.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get('/')
def read_root():
    return {'Hello': 'World'}