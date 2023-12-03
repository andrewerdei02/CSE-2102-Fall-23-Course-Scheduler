# function for students to view their schedule
import json
import boto3

# Initialize DynamoDB clients
dynamodb = boto3.resource('dynamodb')
courses_table = dynamodb.Table('Courses')
user_courses_table = dynamodb.Table('UserCourses')
user_data_table = dynamodb.Table('UserData')

def lambda_handler(event, context):
    if 'httpMethod' in event:
        if event['httpMethod'] == 'POST':
            try:
                # Get user_id from the request body
                body = json.loads(event['body'])
                user_id = body.get('user_id')
                if not user_id:
                    # If user_id is missing, return a 400 Bad Request response
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Please provide a username.')
                    }

                # Check if the user exists in UserData table (you may need to add this based on your setup)
                user_response = user_data_table.get_item(Key={'username': user_id})
                if 'Item' not in user_response:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Invalid username.')
                    }

                # Retrieve the user's courses from UserCourses table
                user_courses = user_courses_table.get_item(Key={'user_id': user_id})
                if 'Item' in user_courses:
                    courses_list = user_courses['Item'].get('courses', [])
                    if not courses_list:
                        return {
                            'statusCode': 404,
                            'body': json.dumps(f'No courses found for user {user_id}.')
                        }
                    
                    # Fetch details for each course ID from the Courses table
                    courses_details = []
                    for course_id in courses_list:
                        course_response = courses_table.get_item(Key={'course_id': course_id})
                        if 'Item' in course_response:
                            courses_details.append(course_response['Item'])
                    
                    return {
                        'statusCode': 200,
                        'body': json.dumps(courses_details)
                    }
                else:
                    return {
                        'statusCode': 404,
                        'body': json.dumps(f'No courses found for user {user_id}.')
                    }
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps(f'Error: {str(e)}')
                }
    # Return a 405 Method Not Allowed response for other HTTP methods
    return {
        'statusCode': 405,
        'body': json.dumps('Method Not Allowed')
    }
