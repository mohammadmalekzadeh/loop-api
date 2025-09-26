# app/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
TEST_DB_URL = os.getenv("TEST_DB_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
BUCKET_ENDPOINT_URL = os.getenv("BUCKET_ENDPOINT_URL")
BUCKET_ACCESS_KEY = os.getenv("BUCKET_ACCESS_KEY")
BUCKET_SECRET_KEY = os.getenv("BUCKET_SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
SMS_API = os.getenv("SMS_API")
SMS_USERNAME = os.getenv("SMS_USERNAME")
SMS_PASSWORD = os.getenv("SMS_PASSWORD")
SMS_NUMBER = os.getenv("SMS_NUMBER")
