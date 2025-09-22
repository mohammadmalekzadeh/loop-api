# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.init_db import init_db
from app.api.v1.endpoints.auth import auth
from app.api.v1.endpoints.user import router as user
from app.api.v1.endpoints.request import request
from app.api.v1.endpoints.adminPanel import router as adminPanel
from app.api.v1.endpoints.profile.dashboard import router as profile
from app.api.v1.endpoints.vendors.vendors import router as vendors
from app.api.v1.endpoints.product.product import router as products

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://loop-ui-nu.vercel.app",
    "https://lloop.ir"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(adminPanel)
app.include_router(auth.router)
app.include_router(user)
app.include_router(request.router)
app.include_router(profile)
app.include_router(vendors)
app.include_router(products)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get('/')
def read_root():
    return {'Hello': 'World'}