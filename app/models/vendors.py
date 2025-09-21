from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class Vendors(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    nation_code = Column(String, unique=True, nullable=True)
    shop_name = Column(String, nullable=True)
    shop_address = Column(Text, nullable=True)
    start_day = Column(String, nullable=True)
    end_day = Column(String, nullable=True)
    start_time = Column(String, nullable=True)
    end_time = Column(String, nullable=True)
    rate = Column(Float, nullable=True, default=0.0)

    user = relationship("User", back_populates="vendors")
    request = relationship("Request", back_populates="vendors")
    product = relationship("Product", back_populates="vendors")