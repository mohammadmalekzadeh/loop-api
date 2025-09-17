from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Vendors(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    nation_code = Column(String, unique=True, nullable=False)
    shop_name = Column(String, nullable=False)
    shop_address = Column(Text, nullable=False)
    start_day = Column(String, nullable=False)
    end_day = Column(String, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)

    user = relationship("User", back_populates="vendors")
    request = relationship("Request", back_populates="vendors")
    product = relationship("Product", back_populates="vendors")