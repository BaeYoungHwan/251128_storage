import requests
from .config import BASE_URL, SEOUL_API_KEY, DATA_TYPE


def fetch_locker_usage(start=1, end=100):
    """
    서울교통공사 물품보관함 이용 데이터 조회
    """
    if not SEOUL_API_KEY:
        raise ValueError("API Key가 설정되지 않았습니다.")

    url = f"{BASE_URL}/{SEOUL_API_KEY}/{DATA_TYPE}/lockerInfo/{start}/{end}"

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise ConnectionError(f"API 요청 실패: {response.status_code}")

    data = response.json()

    # API 에러 메시지 체크
    if "RESULT" in data and data["RESULT"]["CODE"] != "INFO-000":
        raise ValueError(f"API 오류: {data['RESULT']['MESSAGE']}")

    return data
