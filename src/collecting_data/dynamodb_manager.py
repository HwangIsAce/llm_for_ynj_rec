import boto3
from boto3.dynamodb.conditions import Key


class DynamoDBManager:
    def __init__(self, endpoint_url='http://localhost:8000', ):
        self.dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url = endpoint_url,
            # aws_access_key_id ='',
            # aws_secret_access_key ='',
        )
        self.table = None

    # example. need to fix.
    # check the table is well created. => [terminal] aws dynamodb list-tables --endpoint-url http://localhost:8000
    def create_tourism_attraction_table(self):
        table_name = "TourismAttraction"
        # table_name = "TestTable"

        try:
            self.table = self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': 'region', 'KeyType': 'HASH'},  # Partition Key
                    {'AttributeName': 'category#is_open#name', 'KeyType': 'RANGE'}  # Sort Key
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'region', 'AttributeType': 'S'},  # String 타입
                    {'AttributeName': 'category#is_open#name', 'AttributeType': 'S'}  # String 타입
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,  # 초당 최대 5개의 읽기 요청
                    'WriteCapacityUnits': 5  # 초당 최대 5개의 쓰기 요청
                }
            )
            print(f"Creating {table_name} Table...")
            self.table.wait_until_exists()  # 테이블 생성 대기
            print(f"{table_name} Table Creation Complete...!")

        except self.dynamodb.meta.client.exceptions.ResourceInUseException:
            print(f"{table_name} Table already exists.")
            self.table = self.dynamodb.Table(table_name)

        return self.table
 
    def get_table(self, table_name):
        if self.table is None:
            self.table = self.dynamodb.Table(table_name)
        return self.table
    
    # example
    def query_turism_attraction_sites(self, region, prefix):
        if self.table is None:
            raise ValueError("테이블이 존재하지 않습니다. 테이블을 먼저 생성하세요.")
        
        response = self.table.query(
            KeyConditionExpression=Key("region").eq(region) & Key('category#is_open#name').begins_with(prefix)
        )
        return response['Items']

if __name__ == '__main__':
    dynamodb_manager = DynamoDBManager()
    dynamodb_manager.create_tourism_attraction_table() # create a table