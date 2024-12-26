import requests   
import logging      
import pprint       

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def gocamping_basic_information_list_inquiry(base_url, api_key):
    # 기본 정보 목록 조회: 고캠핑 기본정보 목록 조회

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
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

def gocamping_location_based_list_inquiry(base_url, api_key):
    # 위치기반정보 목록 조회: 내주변 좌표를 기반으로 고캠핑정보 목록을 조회

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "mapX": 128.6142847,
        "mapY": 36.0345423,
        "radius": 2000
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


def gocamping_keyword_search_list_inquiry(base_url, api_key):
    # 키워드 검색 목록 조회: 키워드로 검색을 하여 고캠핑정보 목록을 조회

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "keyword": "야영장"
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


def gocamping_image_information_list_inquiry(base_url, api_key):
    # 이미지정보 목록 조회: 각 고캠핑 콘텐츠에 해당하는 이미지URL 목록을 조회

    params = {
        "serviceKey": api_key,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "contentId": 3429
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

    base_url = "http://apis.data.go.kr/B551011/GoCamping/basedList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = gocamping_basic_information_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/GoCamping/locationBasedList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = gocamping_location_based_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/GoCamping/searchList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = gocamping_keyword_search_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)


    base_url = "http://apis.data.go.kr/B551011/GoCamping/imageList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = gocamping_image_information_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)