import csv

from dynamodb_manager import DynamoDBManager

## tourAPI
## csv
def chunk_data(data, chunk_size=25):
    for i in range(0, len(data), chunk_size=chunk_size):
        yield data[i: i+chunk_size]

def change_csv_format(data_path):

    with open(data_path, mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))
        chunk_size = 25

        for chunk in chunk_data(reader, chunk_size):
            with table.batch_writer() as batch:
                for row in batch:
                    # example
                    item={
                        'Region': row['주소'].split(' ')[0], # 서울
                        'Category': row['카테고리'],
                    }
                    batch.put_item(Item=item)

    return f"Chunk of size {len(chunk)} inserted..!"
                
if __name__ == '__main__':
    dynamodb_manager = DynamoDBManager()
    table = dynamodb_manager.get_table('TourismAttraction')
    # table = dynamodb_manager.get_table('TestTable')

    # example
    data = [
        {'region': '서울', 'category#is_open#name': '관광지#open#경복궁', 'details': '조선 왕조의 궁궐'}
    ]

    for item in data:
        table.put_item(Item=item)
        print(f"Insert Successfully..! ")

# check the data well inserted.
# aws dynamodb scan \
#     --table-name TourismFacilities \
#     --endpoint-url http://localhost:8000