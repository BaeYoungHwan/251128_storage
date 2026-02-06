import requests
import db
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
from api_client import fetch_locker_data


# =============================
# 환경설정
# =============================

API_URL = "https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php"
AUTH_KEY = "86OQsBWCRC-jkLAVgtQvUw"

STN = "108"  # 서울 관측소

# DB 접속 정보 (수정 필요)
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "your_db",
    "user": "your_user",
    "password": "your_password"
}


# =============================
# API 데이터 가져오기
# =============================

def fetch_weather():

    params = {
        "stn": STN,
        "authKey": AUTH_KEY
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    return response.text


# =============================
# 데이터 파싱
# =============================

def parse_weather(text):

    lines = text.strip().split("\n")

    data_list = []

    for line in lines:

        # 주석 / 빈줄 제거
        if line.startswith("#") or not line.strip():
            continue

        cols = line.split()

        """
        예시 구조:
        tm wd ws ta hm rn ...
        """

        try:
            tm = cols[0]
            wd = float(cols[2])
            ws = float(cols[3])
            ta = float(cols[11])
            hm = float(cols[13])
            rn = float(cols[15])

            data_list.append(
                (tm, wd, ws, ta, hm, rn)
            )

        except (IndexError, ValueError):
            continue

    return data_list


# =============================
# DB 저장 (UPSERT)
# =============================

def save_to_db(data):
    
    row = data[0]
    
    sql = """
    INSERT INTO storage.weather
    (tm, wd, ws, ta, hm, rn)
    values(:tm, :wd, :ws, :ta, :hm, :rn)
    """
    
    db.execute(sql, {
      "tm": row[0],
      "wd": row[1],
      "ws": row[2],
      "ta": row[3],
      "hm": row[4],
      "rn": row[5]})
    
    
    

    # sql = """
    # INSERT INTO storage.weather
    #     (tm, wd, ws, ta, hm, rn)
    # VALUES %s
    # ON CONFLICT (tm)
    # DO UPDATE SET
    #     wd = EXCLUDED.wd,
    #     ws = EXCLUDED.ws,
    #     ta = EXCLUDED.ta,
    #     hm = EXCLUDED.hm,
    #     rn = EXCLUDED.rn,
    #     reg_dt = CURRENT_TIMESTAMP
    # """

    # execute_values(cur, sql, data)

    # conn.commit()

    # cur.close()
    # conn.close()


# =============================
# 메인 실행
# =============================

def main():

    #print("📡 API 데이터 수집중...")

    text = fetch_weather()

    #print("📄 데이터 파싱중...")

    data = parse_weather(text)

    #print(f"✅ {len(data)}건 수집 완료")

    if not data:
        print("⚠ 저장할 데이터 없음")
        return

    #print("💾 DB 저장중...")

    save_to_db(data)

    
    #print("🎉 저장 완료!")


if __name__ == "__main__":
    main()