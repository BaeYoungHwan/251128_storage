import pandas as pd
from db import execute
from connection import get_engine
CSV_PATH = "data/raw/locker_inventory.csv"
engine = get_engine()
df_stations_db = pd.read_sql("SELECT local_id, local_name FROM storage.local", engine)


# CSV 읽기
df_inventory = pd.read_csv(CSV_PATH, encoding='CP949')
df_inventory = df_inventory.rename(columns={
    "호선":"line_name",
    "보관함명":"local_name",
    "소형":"local_small",
    "중형":"local_middle",
    "대형":"local_large"
})

# stations 기준 merge
df_merged = pd.merge(df_stations_db, df_inventory, on=["local_name","local_name"], how="left")

df_final = df_merged.dropna()
df_final.rename(columns = {"연번" : "inventory_id"}, inplace=True)
df_final.drop("열", inplace= True, axis=1 )

def insert_inventory(pdDF):
    engine = get_engine()

    status = pdDF.to_sql(
    "locker_inventory",
    engine,
    schema = "storage",
    if_exists="append",
    index=False
    )



if __name__ == "__main__":
    insert_inventory(df_final)
    print("inventory insert 완료")