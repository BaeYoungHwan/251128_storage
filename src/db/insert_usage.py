from datetime import datetime
from db import execute
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
from api_client import fetch_locker_data

def insert_locker_usage():
    data = fetch_locker_data(1, 100)
    rows = data["getFcLckr"]["row"]

    sql = """
    INSERT INTO storage.locker_usage
    (station_name, locker_type, used_count, observed_at)
    VALUES (:station_name, :locker_type, :used_count, :observed_at)
    ON CONFLICT DO NOTHING
    """

    for row in rows:
        observed_at = datetime.now()

        for locker_type in ["소형", "중형", "대형"]:
            used = int(row.get(locker_type, 0))

            execute(sql, {
                "station_name": row["STATN_NM"],
                "locker_type": locker_type,
                "used_count": used,
                "observed_at": observed_at
            })


if __name__ == "__main__":
    insert_locker_usage()
    print("locker_usage 수집 완료")
