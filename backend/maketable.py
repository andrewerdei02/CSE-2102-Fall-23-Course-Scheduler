import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='UserData',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# wait until the table exists
table.meta.client.get_waiter('table_exists').wait(TableName='UserData')

print(table.item_count)