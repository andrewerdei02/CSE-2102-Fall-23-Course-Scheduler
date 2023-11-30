# lambda function for fetching courses
import boto3
import json

dynamodb = boto3.resource('dynamodb')
courses_table = dynamodb.Table('Courses')

def lambda_handler(event, context):
    response = courses_table.scan()
    courses = response['Items']
    
    return {
        'statusCode': 200,
        'body': json.dumps(courses)
    }