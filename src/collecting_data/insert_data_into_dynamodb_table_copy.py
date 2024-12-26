import pandas as pd
from decimal import Decimal

from datetime import datetime
from zoneinfo import ZoneInfo

from dynamodb_manager import DynamoDBManager

## tourAPI
## csv
def chunk_data(data, chunk_size=25):
    for i in range(0, len(data), chunk_size):
        yield data[i: i+chunk_size]

def convert_float_to_decimal(obj):
    if isinstance(obj, float):
        return Decimal(str(obj))
    elif isinstance(obj, dict):
        return {key: convert_float_to_decimal(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_float_to_decimal(item) for item in obj]
    else:
        return obj
    
def sanitize_data(data):
    if isinstance(data, float):
        if data != data or data in (float('inf'), float('-inf')):
            return None
        return data
    elif isinstance(data, Decimal):
        if data.is_nan() or data.is_infinite():
            return None
        return data
    elif isinstance(data, dict):
        return {key: sanitize_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]
    else:
        return data

def insert_csv(file_path):
    df = pd.read_csv(file_path)
    df = df[10:20]
    df['source'] = "tourAPI"
    df['category'] = "cultural_facilities"
    dict_list = df.to_dict(orient='records')

    chunk_size = 10
    for chunk in chunk_data(dict_list, chunk_size):
        with table.batch_writer() as batch:
            for row in chunk:
                # example
                common_item={ # hard coding -> parameter 로 받으면 더 좋을 듯
                    'region': row['address'].split(' ')[0], 
                    'category#place_name': f"{row['category']}#{row['place_name']}",
                    # 'address': row['address'],
                    'latitude': row['latitude'],
                    'longitude': row['longitude'],
                    'available_time': row['available_time'],
                    'parking': row['parking'],
                    'description': row['description'],
                    'create_at': datetime.now(ZoneInfo("Asia/Seoul")).isoformat(),
                    'update_at': None,
                }
                common_columns = ['address', 'category', 'place_name', 'latitude', 'longitude', 'available_time', 'parking', 'description']

                unique_item={
                   key: value for key, value in row.items() if (key not in common_columns)
                }

                item = {**common_item, 'attributes': unique_item}

                # preprocess
                item = convert_float_to_decimal(item) # float -> decimal
                item = sanitize_data(item) # NaN -> None
                
                batch.put_item(Item=item)

                print(f"Chunk of size {len(chunk)} inserted..!")

    return f"Completed..!"

def insert_api():

    return f"Completed..!"
                

if __name__ == '__main__':
    dynamodb_manager = DynamoDBManager()
    table = dynamodb_manager.get_table('CulturalFacilites')
    # table = dynamodb_manager.get_table('TestTable')

    file_path = "data/preprocessed_dataset/tourAPI/culturalFacilites.csv"
    insert_csv(file_path)
    # example
    # data = [
    #     {'region': '서울', 'category#available_time#place_name': '관광지#상시개방#경복궁', 'details': '조선 왕조의 궁궐'}
    # ]

# check the data well inserted.
# aws dynamodb scan \
#     --table-name CulturalFacilites \
#     --endpoint-url http://localhost:8000