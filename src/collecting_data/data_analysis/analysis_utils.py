
import numpy as np
import pandas as pd
import requests

def get_geocode(query, client_id, client_secret):
    """address to latitude, longitude."""

    endpoint = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    url = f"{endpoint}?query={query}"

    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
    }

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        try:
            latitude = data['addresses'][0]['y']
            longitude = data['addresses'][0]['x']
            return {'latitude': latitude, 'longitude': longitude}
        except (IndexError, KeyError):
            # return "위도, 경도를 찾을 수 없습니다."
            return np.nan
    else:
        return {"error": res.status_code, "message": res.text}

def get_reverse_geocode(latitude, longitude, client_id, client_secret):
    """latitude, longitude to address."""

    url = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }
    params = {
        "coords": f"{longitude},{latitude}",  
        "output": "json", 
        "orders": "roadaddr,addr" 
    }
    
    res = requests.get(url, headers=headers, params=params)
    
    if res.status_code == 200:
        data = res.json()
        try:
            region_data = data['results'][0]['region']
            area1 = region_data['area1']['name']
            area2 = region_data['area2']['name']
            area3 = region_data['area3']['name']

            building_name = data['results'][0].get('land', {}).get('addition0', {}).get('value', 'No building name')

            full_address = f"{area1} {area2} {area3} {building_name}"
            
            return {'address': full_address}
        except (IndexError, KeyError):
            # return "주소를 찾을 수 없습니다."
            return 
    else:
        return {'error': res.status_code, 'message': res.text}
    
def get_wikipedia_summary(title, language="ko"):
    """tourism attraction to description."""
    url = f"https://{language}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,  # 문서의 첫 번째 문단만 가져옴
        "explaintext": True,  # 텍스트만 반환 (HTML 제외)
        "titles": title,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        pages = data["query"]["pages"]
        for page_id, page_data in pages.items():
            if "extract" in page_data:
                return page_data["extract"]
            else:
                return "설명을 찾을 수 없습니다."
    else:
        return f"API 요청 실패: {response.status_code}"
    
def haversine_vectorized(lat1, lon1, lat2, lon2):
    """calcuate distance using poi"""
    R = 6371
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = np.sin(delta_lat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(delta_lon / 2)**2

    return R**2 * a

def find_nearest_parking(poi_lat, poi_lon, parking_data):
    """poi to nearest parking"""

    latitudes = parking_data['위도'].to_numpy()
    longitudes = parking_data['경도'].to_numpy()

    distances_squared = haversine_vectorized(poi_lat, poi_lon, latitudes, longitudes)

    min_idx = np.argmin(distances_squared)
    nearest_parking = parking_data.iloc[min_idx]
    
    return f"{nearest_parking['주차장명']} {nearest_parking['주차장구분']} 주차장"
