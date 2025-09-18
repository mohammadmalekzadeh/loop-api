# app/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
UI_URL = os.getenv("UI_URL")
TEST_DB_URL = os.getenv("TEST_DB_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGOTIYHM = os.getenv("ALGOTIYHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
