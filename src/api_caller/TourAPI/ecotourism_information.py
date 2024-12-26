import requests   
import logging      
import pprint       

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def region_code_inquiry(base_url, api_key):
    # Function to inquire a list of regional and city/county codes.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "areaCode" : 1,
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


def location_based_ecotourism_information_inquiry(base_url, api_key):
    # Function to inquire a list of eco-tourism information based on region and city/county.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "areaCode" : 2,
        "sigunguCode": 9,
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

if __name__ == "__main__":

    load_dotenv()

    base_url = "http://apis.data.go.kr/B551011/GreenTourService1/areaCode1"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = region_code_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/GreenTourService1/areaBasedList1"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = location_based_ecotourism_information_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)