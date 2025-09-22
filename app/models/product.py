from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    vendors_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    rate = Column(Float, nullable=True, default=0.0)
    buy_freq = Column(Integer, nullable=True, default=0)
    is_active = Column(Boolean, default=True)

    vendors = relationship("Vendors", back_populates="product")
    request = relationship("Request", back_populates="product")
