# app/core/security.py

from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGOTIYHM, SECRET_KEY

def create_access_token(data: dict, expire_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expire or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGOTIYHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGOTIYHM)
        return payload
    except JWTError:
        return None
