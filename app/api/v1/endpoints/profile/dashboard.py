from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User, UserRoleEnum
from app.models.vendors import Vendors
from app.schemas.user import userOption
from app.schemas.vendor import vendorsOption
from app.models.request import Request, RequestStatusEnum
from app.models.product import Product
from app.deps.current_user import get_current_user, get_db
from app.utils.nation_code_check import check_id

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("/user", summary="Get User/Vendors Info")
async def getUser(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    role = UserRoleEnum(current_user.role)
    query = db.query(Request).join(Product).join(Vendors).filter(Request.user_id == current_user.id)

    if role == UserRoleEnum.customer:
        buy_requests = query.filter(Request.status == RequestStatusEnum.accepted).all()

        buy_items = []
        for req in buy_requests:
            buy_items.append({
                "id": req.id,
                "name": req.product.name,
                "type": req.product.type,
                "price": req.product.price,
                "buy_date": req.date.strftime("%Y-%m-%d - %H:%M"),
                "shop": req.vendors.shop_name
            })

        return {
            "id": current_user.id,
            "name": current_user.name,
            "phone": current_user.phone,
            "role": current_user.role,
            "buy_items": buy_items
        }

    if role == UserRoleEnum.vendors:
        vendors = db.query(Vendors).filter(Vendors.user_id == current_user.id).first()

        if not vendors:
            raise HTTPException(status_code=404, detail="Vendor profile not found")

        sell_request = db.query(Product).filter(Product.vendors_id == vendors.id).all()
        sell_items = []
        for p in sell_request:
            sell_items.append({
                "id": p.id,
                "name": p.name,
                "type": p.type,
                "price": p.price,
            })

        buy_request = db.query(Request).join(Product).join(Vendors).filter(Request.vendors_id == vendors.id).filter(Request.status == RequestStatusEnum.accepted).all()
        buy_items = []
        for req in buy_request:
            buy_items.append({
                "id": req.id,
                "name": req.product.name,
                "type": req.product.type,
                "price": req.product.price,
                "buy_date": req.date.strftime("%Y-%m-%d - %H:%M"),    
                "user_name": req.user.name
            })

        return {
            "id": current_user.id,
            "name": current_user.name,
            "phone": current_user.phone,
            "shop_name": vendors.shop_name,
            "shop_address": vendors.shop_address,
            "role": current_user.role,
            "nation_code": vendors.nation_code,
            "start_day": vendors.start_day,
            "end_day": vendors.end_day,
            "start_time": vendors.start_time,
            "end_time": vendors.end_time,
            "sell_items": sell_items,
            "buy_items": buy_items
        }

@router.put("/update/user", summary="Updtae User Info")
async def updateUser(request: userOption, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    
    query = db.query(User).filter(current_user.id == User.id).first()

    query.name = request.name
    query.phone = request.phone

    db.commit()
    db.refresh(query)
    return {"message": "User info updated successfully", "user": current_user}

@router.put("/update/vendors", summary="Updtae and Complete Vendors Info")
async def updateVendors(request: vendorsOption, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user or current_user.role != "vendors":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only vendors can update vendor info")

    vendor = db.query(Vendors).filter(Vendors.user_id == current_user.id).first()
    if not vendor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor profile not found")

    if not check_id(request.nation_code):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Nation Code is incorrect")

    user = db.query(User).filter(current_user.id == User.id).first()
    user.name = request.name
    user.phone = request.phone

    vendor.nation_code = request.nation_code
    vendor.shop_name = request.shop_name
    vendor.shop_address = request.shop_address
    vendor.start_day = request.start_day
    vendor.end_day = request.end_day
    vendor.start_time = request.start_time
    vendor.end_time = request.end_time

    db.commit()
    db.refresh(user)
    db.refresh(vendor)
    return {"message": "Vendor info updated successfully", "vendor": vendor}
