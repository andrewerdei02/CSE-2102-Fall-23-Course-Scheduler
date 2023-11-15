# lambda function for signup
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData')

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        # retrieve data from api gateway
        body = json.loads(event['body'])
        username = body.get('username')
        password = body.get('password')

        # if either username or password is left blank
        if not username or not password:
            return {
                'statusCode': 400,
                'body': 'Both username and password are required. One was left blank.'
            }
        
        # check if the username already exists
        response = table.get_item(Key={'username': username})

        if 'Item' in response:
            return {
                'statusCode': 409,  # conflict - username already exists
                'body': 'An account with this username already exists. Please try again.'
            }

        # if the username doesn't exist, create the new account
        table.put_item(Item={'username': username, 'password': password})

        return {
            'statusCode': 201,  # created
            'body': 'Your account was created succesfully! Go ahead and login!'
        }

    return {
        'statusCode': 405,  # method Not Allowed
        'body': 'Method not allowed'
    }