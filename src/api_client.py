import requests
from config import API_BASE_URL

def fetch_locker_data(start_index=1, end_index=100):
    """
    서울교통공사 물품보관함 API 호출
    """
    url = f"{API_BASE_URL}/{start_index}/{end_index}/"
    response = requests.get(url)

    print("요청 URL:", url)
    print("status:", response.status_code)

    if response.status_code != 200:
        raise Exception(f"API 호출 실패: {response.status_code}")

    return response.text  # ← () 없음
