import requests
from config import API_BASE_URL

def fetch_locker_data(start_index=1, end_index=100):
    """
    서울교통공사 물품보관함 API 호출
    """
    url = f"{API_BASE_URL}/{start_index}/{end_index}/"
    
    response = requests.get(url)
    response.raise_for_status()


    if response.status_code != 200:
        raise Exception(f"API 호출 실패: {response.status_code}")

    return response.json()

"""
data = fetch_locker_data(1,3)
rows = data['response']['body']['items']['item']
for row in rows:
    print(row["lckrId"])
"""
#data = fetch_locker_data(1,3)
#for row in rows:
#    print("--------------------------------------------------------------------------")
#    print(row.get())
