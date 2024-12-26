import requests   
import logging      
import pprint       

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def introduction_information_inquiry(base_url, api_key):
    ### 타입별 소개정보(휴무일, 개장시간, 주차시설 등)를 조회하는 기능입니다.
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


def barrier_free_information_inquiry(base_url, api_key):
    ### Function to inquire detailed information on barrier-free travel.
    ### Provides information for categories such as physical disabilities, visual impairments, hearing impairments, and families with infants.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "contentId": 129619
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
    
    # introduction information inquiry
    base_url = "http://apis.data.go.kr/B551011/KorWithService1/detailIntro1"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = introduction_information_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    # barrier free information inquiry
    base_url = "http://apis.data.go.kr/B551011/KorWithService1/detailWithTour1"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = barrier_free_information_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)