from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, func
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class RequestStatusEnum(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"

class Request(Base):
    __tablename__ = "request"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, unique=True, nullable=False)
    vendors_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    count = Column(Integer, nullable=False, default=1)
    date = Column(DateTime, server_default=func.now())
    status = Column(Enum(RequestStatusEnum), default=RequestStatusEnum.pending)

    product = relationship("Product", back_populates="request")
    user = relationship("User", back_populates="request")
    vendors = relationship("Vendors", back_populates="request")
