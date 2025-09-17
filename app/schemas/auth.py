from pydantic import BaseModel
from typing import Optional

class LoginRequest(BaseModel):
    phone: str

class VerifyRequest(BaseModel):
    phone: str
    otp_code: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class SignupRequest(BaseModel):
    phone: str
    name: str