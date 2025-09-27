from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func, desc, asc
from app.models.request import Request, RequestStatusEnum
from app.schemas.request import RequestCreate, RequestOut, filterRequest
from app.models.user import User, UserRoleEnum
from app.models.product import Product
from app.models.vendors import Vendors
from app.deps.current_user import get_current_user, get_db
from typing import List
import random
from khayyam import JalaliDatetime
from app.utils.sms_sender import sms_sender
from app.utils.sms_text import request_customer_sms, request_vendors_sms

router = APIRouter(prefix="/request", tags=["Request"])

@router.post("/create")
async def create_request(
    req: RequestCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role == UserRoleEnum.vendors:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vendors couldn't create a request")

    unique_code = random.randint(100000, 999999)
    while db.query(Request).filter(Request.code == unique_code).first():
        unique_code = random.randint(100000, 999999)
    
    product = db.query(Product).filter(Product.id == req.product_id).first()

    if product.inventory == req.count: product.inventory = 0; product.is_active = False
    else: product.inventory -= req.count

    new_request = Request(
        code=unique_code,
        vendors_id=product.vendors_id,
        user_id=current_user.id,
        product_id=req.product_id,
        count=req.count,
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    db.refresh(product)

    # send sms for request to customer
    sms_sender(phone= current_user.phone, message= request_vendors_sms(product_name= product.name, request_code= new_request.code, request_count= new_request.count))

    # send sms for request to vendprs
    vendors = db.query(Vendors).join(Product).filter(Vendors.id == Product.vendors_id).first()
    sms_sender(phone= vendors.user.phone, message= request_vendors_sms(product_name= product.name, request_code= new_request.code, request_count= new_request.count))

    return new_request


@router.get("/show", response_model=List[RequestOut])
async def get_requests(
    filter: filterRequest = Depends(),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_role = UserRoleEnum(current_user.role)

    if user_role == UserRoleEnum.customer:
        requests = db.query(Request).filter(Request.user_id == current_user.id)
    else:
        requests = db.query(Request).join(Request.vendors).filter(Vendors.user_id == current_user.id)

    if filter.status:
        requests = requests.filter(Request.status == RequestStatusEnum.accepted if filter.status == "accepted" else Request.status == RequestStatusEnum.pending)
    if filter.date:
        requests = requests.order_by(asc(Request.date) if filter.date == "old" else desc(Request.date))
    if filter.code:
        requests = requests.filter(Request.code == filter.code)

    result = []
    for r in requests.all():
        result.append({
            "id": r.id,
            "role": current_user.role,
            "code": r.code,
            "product_name": r.product.name,
            "vendors_name": r.vendors.user.name,
            "address": r.vendors.shop_address,
            "customer_name": r.user.name,
            "count": r.count,
            "date": r.date,
            "jalali_date": JalaliDatetime(r.date).strftime("%Y/%m/%d - %H:%M"),
            "status": r.status,
            "price": r.product.price * r.count,
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

    if current_user.role == UserRoleEnum.vendors and req.vendors_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="FORBIDDEN")
    if current_user.role == UserRoleEnum.customer and req.user_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="FORBIDDEN")

    product = db.query(Product).filter(Product.id == req.product_id).first()
    vendors = db.query(Vendors).filter(req.vendors_id == product.vendors_id).first()
    vendors.income += req.count * product.price

    product.buy_freq =+ req.count
    req.status = status_value

    db.commit()
    db.refresh(req)
    db.refresh(product)
    db.refresh(vendors)

    return {"message": "وضعیت با موفقیت تغییر کرد", "status": req.status}

@router.post("/{request_id}")
async def postRate(
        request_id: int,
        rate: float,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user),
):
    request = db.query(Request).filter(Request.id == request_id).first()

    if current_user.id != request.user_id:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="UNAUTHORIZED")

    vendors = db.query(Vendors).filter(request.vendors_id == Vendors.id).first()
    product = db.query(Product).filter(request.product_id == Product.id).first()

    vendors.rate = round((vendors.rate + rate) / 2, 2) if vendors.rate != 0 else rate
    product.rate = round((product.rate + rate), 2) / 2 if product.rate != 0 else rate

    db.commit()
    db.refresh(vendors)
    db.refresh(product)
