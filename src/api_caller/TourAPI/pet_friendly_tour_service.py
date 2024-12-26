import requests   
import logging      
import pprint       

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def introduction_information_inquiry(base_url, api_key):
    ### 반려 동물 동반여행지의 타입별 소개정보(휴무일, 개장시간, 주차시설 등)를 조회하는 기능입니다.
    ### 각 타입마다 응답 항목이 다르게 제공됩니다.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "contentId": 1059479,
        "contentTypeId": 12,
        "defaultYN": "Y",
        "firstImageYN": "Y",
        "areacodeYN": "Y",
        "catcodeYN": "Y",
        "addrinfoYN": "Y",
        "mapinfoYN": "Y",
        "overviewYN": "Y"

    }

    response = requests.get(base_url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.text
        logging.info("API call successful!")
        logging.info(f"response data: {data}")
        return data
    else:
        logging.error(f"API call fail...: {response.status_code}")
        return None


def introduction_information_inquiry(base_url, api_key):
    ### 반려 동물 동반여행지의 타입별 소개정보(휴무일, 개장시간, 주차시설 등)를 조회하는 기능입니다.
    ### 각 타입마다 응답 항목이 다르게 제공됩니다.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "contentId": 1059479,
        "_type": "json",
        "contentTypeId": 12
    }

    response = requests.get(base_url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.text
        logging.info("API call successful!")
        logging.info(f"response data: {data}")
        return data
    else:
        logging.error(f"API call fail...: {response.status_code}")
        return None


def repetitive_information_inquiry(base_url, api_key):
    ### 반려 동물 동반여행지의 타입별 반복정보를 조회하는 기능입니다.
    ### “숙박”은 객실정보를 제공합니다.
    ### “숙박를 제외한 나머지 타입은 다양한 정보를 반복적인 형태로 제공합니다.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "contentId": 1059479,
        "_type": "json",
        "contentTypeId": 12
    }

    response = requests.get(base_url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.text
        logging.info("API call successful!")
        logging.info(f"response data: {data}")
        return data
    else:
        logging.error(f"API call fail...: {response.status_code}")
        return None


def pet_friendly_tour_inquiry(base_url, api_key):
    ### Function to inquire detailed information on pet-friendly travel.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "contentId": 1059479,
        "_type": "json",
    }

    response = requests.get(base_url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.text
        logging.info("API call successful!")
        logging.info(f"response data: {data}")
        return data
    else:
        logging.error(f"API call fail...: {response.status_code}")
        return None

if __name__ == "__main__":
    
    load_dotenv()

    base_url = "http://apis.data.go.kr/B551011/KorPetTourService/detailCommon"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = introduction_information_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/KorPetTourService/detailInfo"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = introduction_information_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/KorPetTourService/detailInfo"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = repetitive_information_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/KorPetTourService/detailPetTour"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = pet_friendly_tour_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)