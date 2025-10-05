# app/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 10080))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))
BUCKET_ENDPOINT_URL = os.getenv("BUCKET_ENDPOINT_URL")
BUCKET_ACCESS_KEY = os.getenv("BUCKET_ACCESS_KEY")
BUCKET_SECRET_KEY = os.getenv("BUCKET_SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
SMS_API = os.getenv("SMS_API")
SMS_SENDER = os.getenv("SMS_SENDER")
