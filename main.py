# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.db.init_db import init_db
from app.api.v1.endpoints.auth import auth
from app.api.v1.endpoints.user import router as user
from app.api.v1.endpoints.request import request
from app.api.v1.endpoints.adminPanel import router as adminPanel
from app.api.v1.endpoints.profile.dashboard import router as profile
from app.api.v1.endpoints.vendors.vendors import router as vendors
from app.api.v1.endpoints.product.product import router as products
from app.api.v1.endpoints.vendors.upload_avatar import router as upload_avatar

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "https://loop-ui-nu.vercel.app",
    "https://lloop.ir",
    "http://lloop.ir",
    "https://www.lloop.ir",
    "http://www.lloop.ir",
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
app.include_router(upload_avatar)

@app.get('/')
def read_root():
    return {'Hello': 'World'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)