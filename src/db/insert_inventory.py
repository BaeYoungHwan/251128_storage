import pandas as pd
from db import execute

CSV_PATH = "data/raw/locker_inventory.csv"

def insert_inventory():
    df = pd.read_csv(CSV_PATH, encoding='cp949')

    sql = """
    INSERT INTO storage.locker_inventory
    (station_name, line, locker_name, locker_type, total_count)
    VALUES (:station_name, :line, :locker_name, :locker_type, :total_count)
    """

    for _, row in df.iterrows():
        for locker_type, col in [
            ("small", "소형"),
            ("medium", "중형"),
            ("large", "대형")
        ]:
            count = row[col]
            if pd.isna(count) or count == 0:
                continue

            execute(sql, {
                "station_name": row["보관함명"],
                "line": row["호선"],
                "locker_name": row["보관함명"],
                "locker_type": locker_type,
                "total_count": int(count)
            })


if __name__ == "__main__":
    insert_inventory()
    print("inventory insert 완료")