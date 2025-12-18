import os
from dotenv import load_dotenv
import psycopg2
from datetime import datetime

# .env 로드
load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()

# 테스트 데이터
test_data = {
    "station_id": 636,
    "station_name": "약수(6호선)",
    "line_name": "6호선",
    "created_at": datetime.now()
}

insert_query = """
INSERT INTO storage.stations
(station_id, station_name, line_name, created_at)
VALUES (%s, %s, %s, %s)
"""

cursor.execute(insert_query, (
    test_data["station_id"],
    test_data["station_name"],
    test_data["line_name"],
    test_data["created_at"]
))

conn.commit()

cursor.close()
conn.close()

print("✅ 테스트 데이터 삽입 완료")