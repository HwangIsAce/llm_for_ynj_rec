from dynamodb_manager import DynamoDBManager

if __name__ == "__main__":
    dynamodb_manager = DynamoDBManager()
    dynamodb_manager.get_table('TestTable')
    
    items = dynamodb_manager.query_turism_attraction_sites(region='서울', prefix='관광지')

    for item in items:
        print(item)



