# lambda function for login
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData') 

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        # get data from api gateway
        data = json.loads(event['body'])
        username = data['username']
        password = data['password']
        
        # check if username or password was left blank
        if not username or not password:
            return {
                'statusCode': 400,
                'body': 'Both username and password are required. One was left blank.'
            }

        response = table.get_item(Key={'username': username})
    
        if 'Item' in response:
            user_data = response['Item']
            # if both username and password match, successful login
            if user_data['password'] == password:
                return {
                    'statusCode': 200,
                    'body': 'You have succesfully logged in!'
                }
            # otherwise, username matches but password is incorrect
            else:
                return {
                    'statusCode': 401,
                    'body': 'The password you entered is incorrect.'
                }
        # if no conditions pass, the username must not exist at all
        else:
            return {
                'statusCode': 404,
                'body': 'The username you entered does not exist.'
            }
