from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.vendors import Vendors
from app.models.user import User
from app.models.product import Product
from app.schemas.vendor import vendorsFilter
from app.deps.current_user import get_db

router = APIRouter(prefix="/vendors", tags=["Vendors"])

@router.get("", summary="Get all Vendors")
async def getVendors(filter: vendorsFilter = Depends(), db: Session = Depends(get_db)):
    query = db.query(Vendors)

    if filter.rate:
        query = query.order_by(Vendors.rate.desc() if filter.rate == "max" else Vendors.rate.asc())
    if filter.is_work:
        query = query.join(Product, Vendors.id == Product.vendors_id).group_by(Vendors.id).order_by(func.count(Product.id).desc())

    result = []
    for v in query.all():
        result.append({
            "id": v.id,
            "name": v.user.name if v.user else None,
            "shop_name": v.shop_name,
            "shop_address": v.shop_address,
            "start_day": v.start_day,
            "end_day": v.end_day,
            "start_time": v.start_time,
            "end_time": v.end_time,
            "rate": v.rate,
            "products": [
                {
                    "id": p.id,
                    "name": p.name,
                    "type": p.type,
                    "price": p.price,
                    "buy_freq": p.buy_freq,
                    "rate": p.rate,
                }
                for p in v.product
            ]
        })

    return result

@router.get("/products/{vendors_id}", summary="Get Vendors Products")
async def getVendorsProducts(vendors_id: int, db: Session = Depends(get_db)):
    query = db.query(Vendors).filter(Vendors.id == vendors_id).first()

    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendors not found")

    results = {
        "name": query.user.name if query.user else None,
        "shop_name": query.shop_name,
        "shop_address": query.shop_address,
        "start_day": query.start_day,
        "end_day": query.end_day,
        "start_time": query.start_time,
        "end_time": query.end_time,
        "rate": query.rate,
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "type": p.type,
                "price": p.price,
                "buy_freq": p.buy_freq,
                "rate": p.rate,
                "inventory": p.inventory
            }
            for p in query.product
        ]
    }

    return results
