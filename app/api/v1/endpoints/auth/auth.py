from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.session import SessionLocal
from app.models.user import User, UserRoleEnum
from app.schemas.auth import LoginRequest, TokenResponse, VerifyRequest, SignupRequest
from app.utils.otp import generate_otp
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
async def signup(request: SignupRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == request.phone).first()
    
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"data": "User exist"})
    
    role = UserRoleEnum(request.role)

    user = User(phone=request.phone, name=request.name, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)

    otp = generate_otp()
    user.set_otp(otp)
    db.commit()

    # SMS
    return {"otp": otp}

@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == request.phone).first()
    
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail={"data" : "User not found"})
    
    otp = generate_otp()
    user.set_otp(otp)
    db.commit()

    # SMS
    return {"otp": otp}

@router.post("/verify", response_model= TokenResponse)
async def verify(request: VerifyRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == request.phone).first()

    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail={"data" : "User not found"})

    if user.otp_code != request.otp_code:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail={"data" : "Invalid OTP"})
    
    if user.otp_expiration < datetime.utcnow():
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail={"data" : "OTP expire"})

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
