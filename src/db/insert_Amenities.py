import pandas as pd
from db import execute
from connection import get_engine
CSV_PATH = "data/raw/local_Amenities.csv"
engine = get_engine()
df_stations_db = pd.read_sql("SELECT station_id, station_name, line_name FROM storage.local", engine)

df_Amenities = pd.read_csv(CSV_PATH, encoding='CP949')
df_Amenities = df_Amenities.rename(columns={

    "지하철역ID" : "station_id",
    "지하철역명" : "station_name",
    "호선" : "line_name",
    "엘리베이터유무" : "elevator",
    "휘체어리프트유무" : "wheelchairlift",
    "환승주차자유무" : "parking",
    "무인민원발급기유무" : "complaint",
    "환전키오스크유무" : "exchange",
    "기차예매역유무" : "trainreservation",
    "문화공간유무" : "culturalspace",
    "만남의장소유무" : "meeting",
    "유아수유방유무" : "lactation"

})


# stations 기준 merge
df_merged = pd.merge(df_stations_db, df_Amenities, on=["station_name","station_name"], how="left")


def insert_Amenities(pdDF):
    engine = get_engine()

    status = pdDF.to_sql(
    "local_Amenities",
    engine,
    schema = "storage",
    if_exists="append",
    index=False
    )

df_merged.drop(['station_id_y','line_name_y'], axis=1, inplace=True)
df_merged = df_merged.rename(columns={

    "station_id" : "station_id_x",
    "line_name" : "line_name_x",


})

df_merged.to_csv('merge.csv', index=False, encoding='utf-8-sig')


# if __name__ == "__main__":
#     insert_Amenities(df_final)
#     print("inventory insert 완료")
