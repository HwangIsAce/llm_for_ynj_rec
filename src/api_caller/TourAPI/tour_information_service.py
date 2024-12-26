import requests
import logging
import pprint

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def location_based_tourist_information_inquiry(base_url, api_key):
    ### description ###

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "baseYm": 202408,
        "areaCd": 11,
        "signguCd": 11530,
        "_type": "json",
    }
    # params = {
    #     "serviceKey": api_key,
    #     "pageNo": 1,
    #     "MobileOS": "ETC",
    #     "MobileApp": "AppTest",
    #     "_type": "json",
    #     "listYN": "Y",
    #     "arrange": "A", 
    #     "mapX": 126.961611,
    #     "mapY": 37.568477,
    #     "radius": 1000,
    #     "contentTypeId": 15,
    # }

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
    
    base_url = "http://apis.data.go.kr/B551011/TarRlteTarService/areaBasedList?"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = location_based_tourist_information_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)