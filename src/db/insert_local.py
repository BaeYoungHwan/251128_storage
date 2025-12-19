from datetime import datetime
from db import execute
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
from api_client import fetch_locker_data

def insert_local():
   data = fetch_locker_data(1, 1000)
   rows = data['response']['body']['items']['item']

   sql = """
    INSERT INTO storage.local
    (local_id, local_name, station_id, station_name, line_name)
    VALUES (:local_id, :local_name, :station_id, :station_name, :line_name)
    """
   

   for row in rows:
      local_name = row["lckrRprsLocNm"][4:]
      local_name = local_name.replace( '(','')
      local_name = local_name.replace( ')','')
      execute(sql, {
      "local_id": row["lckrId"],
      "local_name": local_name,
      "station_id": row["stnNo"],
      "station_name": row["stnNm"],
      "line_name": row["lineNm"]
   })
      

 
#if __name__ == "__main__":
#   insert_local()
#   print("locker_usage 수집 완료")

