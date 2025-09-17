from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime, timedelta

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    otp_code = Column(String, nullable=True)
    otp_expiration = Column(DateTime, nullable=True)

    request = relationship("Request", back_populates="user")

    def set_otp(self, code: str):
        self.otp_code = code
        self.otp_expiration = datetime.utcnow() + timedelta(minutes=5)