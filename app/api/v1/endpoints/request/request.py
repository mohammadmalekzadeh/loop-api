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

@router.post("/create", response_model=RequestOut)
async def create_request(
    req: RequestCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_role = current_user.role

    if user_role == "vendors":return status.HTTP_400_BAD_REQUEST

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
    
    requests = db.query(Request).filter(Request.user_id == current_user.id).join(Product, Product.id == Request.product_id).join(Vendors, Vendors.id == Request.vendors_id)

    # تبدیل به دیکشنری برای فرانت
    result = []
    for r in requests:
        result.append({
            "id": r.id,
            "code": r.code,
            "product_name": r.product.name if r.product else None,
            "vendor_name": r.vendors.name if r.vendors else None,
            "customer_name": r.user.name if r.user else None,
            "count": r.count,
            "date": r.date.strftime("%Y-%m-%d %H:%M"),
            "status": r.status.value
        })

    return result
