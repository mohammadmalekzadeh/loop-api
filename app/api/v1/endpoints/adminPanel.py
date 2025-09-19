from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.deps.current_user import get_db
from app.models.user import User
from app.models.product import Product
from app.models.vendors import Vendors
from app.models.request import Request

router = APIRouter(prefix="/admin/panel", tags=["Admin Panel"])

@router.get("/user/all", summary="Get All data of User")
async def getUserAll(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/vendors/all", summary="Get All data of Vendors")
async def getVendorsAll(db: Session = Depends(get_db)):
    return db.query(Vendors).all()

@router.get("/product/all", summary="Get All data of Product")
async def getProductAll(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/request/all", summary="Get All data of Request")
async def getRequestAll(db: Session = Depends(get_db)):
    return db.query(Request).all()
