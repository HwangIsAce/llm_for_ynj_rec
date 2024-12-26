import requests   
import logging      
import pprint       

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def tour_photo_gallery_list_inquiry(base_url, api_key):
    ### Function to inquire a list of photo galleries.
    ### Groups content by title to remove duplicates and provides a list including details such as photo URL path, shooting month, and shooting location.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "arrange" : "A",
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


def tour_photo_gallery_detailed_list_inquiry(base_url, api_key):
    ### Function to inquire a detailed list of photo galleries.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "title": "%EC%9D%B4%ED%83%9C%EC%9B%90%EA%B1%B0%EB%A6%AC"
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


def tour_photo_gallery_keyword_search_list_inquiry(base_url, api_key):
    ### Function to inquire a list of tourism photo galleries through keyword search.
    ### Retrieves a list of photo galleries that match the keyword data, displaying grouped information based on titles.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "arrange" : "A",
        "MobileApp": "AppTest",
        "_type": "json",
        "keyword": "서울 야경 축제"
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

    base_url = "http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = tour_photo_gallery_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)


    base_url = "http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryDetailList1"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = tour_photo_gallery_detailed_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1"
    api_key = os.getenv("TOURAPI_API_KEY")
    
    sample = tour_photo_gallery_keyword_search_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)