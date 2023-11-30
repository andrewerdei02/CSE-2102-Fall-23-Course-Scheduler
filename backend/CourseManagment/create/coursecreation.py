# lambda function for signup
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Courses')

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        # retrieve data from api gateway
        body = json.loads(event['body'])
        course_id = body.get('course_id')
        course_name = body.get('course_name')
        total_seats = body.get('total_seats')

        # if either username or password is left blank
        if not course_id or not course_name or not total_seats:
            return {
                'statusCode': 400,
                'body': 'Both username and password are required. One was left blank.'
            }
        
        # check if the username already exists
        response = table.get_item(Key={'course_id': course_id})

        if 'Item' in response:
            return {
                'statusCode': 409,  # conflict - username already exists
                'body': 'An account with this username already exists. Please try again.'
            }

        # if the username doesn't exist, create the new account
        table.put_item(Item={'course_id': course_id, 'course_name': course_name, 'total_seats': total_seats})

        return {
            'statusCode': 201,  # created
            'body': 'Your account was created succesfully! Go ahead and login!'
        }

    return {
        'statusCode': 405,  # method Not Allowed
        'body': 'Method not allowed'
    }