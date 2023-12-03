# function for admin to create a course
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Courses')

def lambda_handler(event, context):
    if 'httpMethod' in event:
        if event['httpMethod'] == 'POST':
            body = json.loads(event['body'])
            course_id = body.get('course_id')
            course_name = body.get('course_name')
            total_seats = body.get('total_seats')
            professor_name = body.get('professor_name')  
            days_of_week = body.get('days_of_week')      
            class_time = body.get('class_time')          

            if not course_id or not course_name or not total_seats or not professor_name or not days_of_week or not class_time:
                return {
                    'statusCode': 400,
                    'body': 'All fields ( are required.'
                }

            response = table.get_item(Key={'course_id': course_id})

            if 'Item' in response:
                return {
                    'statusCode': 409,
                    'body': 'A course with this ID already exists. Please use a different ID.'
                }

            item = {
                'course_id': course_id,
                'course_name': course_name,
                'total_seats': total_seats,
                'professor_name': professor_name,  
                'days_of_week': days_of_week,    
                'class_time': class_time         
            }

            table.put_item(Item=item)

            return {
                'statusCode': 201,
                'body': 'The course was created successfully!'
            }

        return {
            'statusCode': 405,
            'body': 'Only POST method is allowed for this endpoint.'
        }
    else:
        return {
            'statusCode': 400,
            'body': 'Invalid request format: Missing httpMethod in the event.'
        }
