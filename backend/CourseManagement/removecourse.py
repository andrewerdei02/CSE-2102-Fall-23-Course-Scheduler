# function for admin to remove a course
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Courses')

def lambda_handler(event, context):
    # Check if 'httpMethod' key is present in the event
    if 'httpMethod' in event:
        if event['httpMethod'] == 'DELETE':
            # Retrieve data from API Gateway
            body = json.loads(event['body'])
            course_id = body.get('course_id')

            # If course_id is missing in the request body
            if not course_id:
                return {
                    'statusCode': 400,
                    'body': 'Course ID is required in the request body for DELETE request.'
                }

            # Check if the course exists
            response = table.get_item(Key={'course_id': course_id})

            if 'Item' not in response:
                return {
                    'statusCode': 404,  # Not Found
                    'body': 'Course not found with the provided course_id.'
                }

            # If the course exists, delete it
            table.delete_item(Key={'course_id': course_id})

            return {
                'statusCode': 200,
                'body': 'The course was deleted successfully!'
            }

        return {
            'statusCode': 405,  # Method Not Allowed
            'body': 'Only DELETE method is allowed for this endpoint.'
        }
    else:
        return {
            'statusCode': 400,
            'body': 'Invalid request format: Missing httpMethod in the event.'
        }