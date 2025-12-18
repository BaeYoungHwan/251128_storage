import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 읽기

# PostgreSQL 설정
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# API 설정
API_KEY = os.getenv("SEOUL_API_KEY")
API_BASE_URL = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/getFcLckr"

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}