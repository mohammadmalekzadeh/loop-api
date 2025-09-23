from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Optional
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.vendors import Vendors
from app.models.user import User, UserRoleEnum
from app.models.product import Product
from app.schemas.product import createProducts, updateProducts, filterProducts
from app.deps.current_user import get_db, get_current_user

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("", summary="Get all products")
async def getProducts(filter: filterProducts = Depends(), db: Session = Depends(get_db)):
    query = db.query(Product).filter(Product.is_active == True)

    if filter.type:
        query = query.filter(Product.type == filter.type)
    if filter.shop_name:
        query = query.join(Vendors, Vendors.id == Product.vendors_id).filter(Vendors.shop_name == filter.shop_name)
    if filter.price:
        query = query.order_by(Product.price.desc() if filter.price == "max" else Product.price.asc())
    if filter.rate:
        query = query.order_by(Product.rate.desc() if filter.rate == "max" else Product.rate.asc())
    if filter.is_popular:
        query = query.order_by(Product.buy_freq.desc())

    results = []
    for r in query.all():
        results.append({
            "id": r.id,
            "name": r.name,
            "type": r.type,
            "vendor": r.vendors.user.name,
            "shop": r.vendors.shop_name,
            "address": r.vendors.shop_address,
            "price": r.price,
            "rate": r.rate,
            "buy_freq": r.buy_freq,
            "inventory": r.inventory
        })

    return results

@router.post("/create", summary="Post a new Products")
async def postProducts(request: createProducts, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != UserRoleEnum.vendors:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't access")
    
    vendors = db.query(Vendors).filter(Vendors.user_id == current_user.id).first()

    if vendors.nation_code is None or vendors.shop_name is None or vendors.shop_address is None:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="405_METHOD_NOT_ALLOWED")
    
    product = Product(
        vendors_id= vendors.id,
        name= request.name,
        type= request.type,
        price= request.price,
        is_active= True,
        inventory= request.inventory,
        )
    
    db.add(product)
    db.commit()
    db.refresh(product)

@router.put("/is_active/{product_id}")
async def activeUpdate(is_active: bool, product_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.vendors.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    if product.inventory == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inventory is Zero")

    product.is_active = is_active
    db.commit()
    db.refresh(product)

    return {"message": "Product updated", "is_active": product.is_active}

@router.put("/edit", summary="Product edit")
async def editProduct():
    ...
