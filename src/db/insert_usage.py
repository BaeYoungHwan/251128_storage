from datetime import datetime
#from db import execute
import db
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
from api_client import fetch_locker_data

def insert_usage():
   
   data = fetch_locker_data(1, 1000)
   rows = data['response']['body']['items']['item']

   sql = """
    INSERT INTO storage.locker_usage
    (station_name, local_id, local_name, able_small, able_middle, able_large, observed_at)
    VALUES (:station_name, :local_id, :local_name, :able_small, :able_middle, :able_large, :observed_at)
    """
   

   for row in rows:
      local_name = row["lckrRprsLocNm"][4:]
      local_name = local_name.replace( '(','')
      local_name = local_name.replace( ')','')
      
      db.execute(sql, {
      "station_name": row["stnNm"],
      "local_id": row["lckrId"],
      "local_name": local_name,
      "able_small": row["usePsbltySmttypeLckrCnt"],
      "able_middle": row["usePsbltyMdtypeLckrCnt"],
      "able_large": row["usePsbltyLrtypeLckrCnt"],
      "observed_at": row["totCrtrDt"]})
      

 
if __name__ == "__main__":
   insert_usage()
   print("insert_usage 입력 완료")

