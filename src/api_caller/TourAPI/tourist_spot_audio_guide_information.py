import requests   
import logging      
import pprint    

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def tourist_basic_information_list_inquiry(base_url, api_key):
    ### Function to inquire a list of basic information about tourist sites.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "langCode": "ko"
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


def location_based_tourist_spot_information_list_inquiry(base_url, api_key):
    ### Function to inquire a list of tourist information based on nearby coordinates.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "langCode": "ko",
        "mapX": 126.615455,
        "mapY": 34.476566,
        "radius": 1000

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


def tourist_spot_keyword_search_list_inquiry(base_url, api_key):
    ### Function to inquire a list of tourist information by searching with a keyword.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "langCode": "ko",
        "keyword": "대흥사"

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


def story_basic_information_list_inquiry(base_url, api_key):
    ### Function to inquire a list of basic information about stories.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "langCode": "ko",
        "tid": 2588,
        "tlid": 2588
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


def story_location_based_information_list_inquiry(base_url, api_key):
    ### Function to inquire a list of story information based on nearby coordinates.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "langCode": "ko",
        "mapX": 126.615455,
        "mapY": 34.476566,
        "radius": 1000

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


def story_keyword_search_list_inquiry(base_url, api_key):
    ### Function to inquire a list of story information by searching with a keyword.

    params = {
        "serviceKey": api_key,
        "pageNo": 1,
        "numOfRows": 10,
        "MobileOS" : "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "langCode": "ko",
        "keyword": "대흥사"

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

    base_url = "http://apis.data.go.kr/B551011/Odii/themeBasedList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = tourist_basic_information_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/Odii/themeLocationBasedList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = location_based_tourist_spot_information_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)


    base_url = "http://apis.data.go.kr/B551011/Odii/themeSearchList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = tourist_spot_keyword_search_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/Odii/storyBasedList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = story_basic_information_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/Odii/storyLocationBasedList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = story_location_based_information_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)

    base_url = "http://apis.data.go.kr/B551011/Odii/storySearchList"
    api_key = os.getenv("TOURAPI_API_KEY")

    sample = story_keyword_search_list_inquiry(base_url=base_url, api_key=api_key)
    if sample:
        pprint.pprint(sample)