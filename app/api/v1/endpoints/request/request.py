from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.request import Request, RequestStatusEnum
from app.schemas.request import RequestCreate, RequestOut
from app.models.user import User
from app.models.product import Product
from app.models.vendors import Vendors
from app.deps.current_user import get_current_user, get_db
from typing import List
import random

router = APIRouter(prefix="/request", tags=["Request"])

@router.post("/create")
async def create_request(
    req: RequestCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_role = current_user.role

    if user_role == "vendors":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vendors couldn't create a request")

    unique_code = random.randint(100000, 999999)
    while db.query(Request).filter(Request.code == unique_code).first():
        unique_code = random.randint(100000, 999999)
    
    new_request = Request(
        code=unique_code,
        vendors_id=req.vendors_id,
        user_id=current_user.id,
        product_id=req.product_id,
        count=req.count,
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request


@router.get("/show", response_model=List[RequestOut])
async def get_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_role = current_user.role
    status
    
    requests = db.query(Request).join(Product).join(Vendors).filter(Request.user_id == current_user.id).all()

    result = []
    for r in requests:
        result.append({
            "id": r.id,
            "code": r.code,
            "product_name": r.product.name,
            "vendor_name": r.vendors.shop_name,
            "address": r.vendors.address,
            "customer_name": r.user.name,
            "count": r.count,
            "date": r.date.strftime("%Y-%m-%d %H:%M"),
            "status": r.status
        })

    return result

@router.put("/update/{request_id}")
async def update_request_status(
    request_id: int,
    status_value: RequestStatusEnum,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    req = db.query(Request).filter(Request.id == request_id).first()
    if not req:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Request not found")

    if current_user.role == "vendors" and req.vendors_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="FORBIDDEN")
    if current_user.role == "customer" and req.user_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="FORBIDDEN")

    req.status = status_value
    db.commit()
    db.refresh(req)

    return {"message": "وضعیت با موفقیت تغییر کرد", "status": req.status}

