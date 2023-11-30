# lambda function for fetching a specific user's courses
import boto3
import json

dynamodb = boto3.resource('dynamodb')
user_courses_table = dynamodb.Table('UserCourses')

def lambda_handler(event, context):
    user_id = event['user_id']
    
    response = user_courses_table.get_item(Key={'user_id': user_id})
    if 'Item' in response:
        user_courses = response['Item'].get('courses', [])
        return {
            'statusCode': 200,
            'body': json.dumps(user_courses)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('User not found or no courses found for this user!')
        }
