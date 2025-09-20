from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime, timedelta
import enum

class UserRoleEnum(str, enum.Enum):
    vendoers = "vendors"
    customer = "customer"

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    role = Column(Enum(UserRoleEnum, name="userroleenum"), default= UserRoleEnum.customer)
    otp_code = Column(String, nullable=True)
    otp_expiration = Column(DateTime, nullable=True)

    request = relationship("Request", back_populates="user")
    vendors = relationship("Vendors", back_populates="user")

    def set_otp(self, code: str):
        self.otp_code = code
        self.otp_expiration = datetime.utcnow() + timedelta(minutes=5)