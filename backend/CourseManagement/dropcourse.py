# function for students to drop a course from schedule
import json
import boto3

# Initialize DynamoDB clients
dynamodb = boto3.resource('dynamodb')
courses_table = dynamodb.Table('Courses')
user_courses_table = dynamodb.Table('UserCourses')
user_data_table = dynamodb.Table('UserData')

def lambda_handler(event, context):
    if 'httpMethod' in event:
        if event['httpMethod'] == 'DELETE':
            # Get data from the API request
            try:
                body = json.loads(event['body'])
                drop_user_id = body.get('drop_user_id')
                drop_course_id = body.get('drop_course_id')
                
                # Check if drop_user_id or drop_course_id is missing
                if not drop_user_id or not drop_course_id:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Please provide both username and course ID to drop.')
                    }
                
                # Check if the user exists in UserData table
                user_response = user_data_table.get_item(Key={'username': drop_user_id})
                if 'Item' not in user_response:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Invalid username.')
                    }
                
                # Check if the course exists in Courses table
                course_response = courses_table.get_item(Key={'course_id': drop_course_id})
                if 'Item' not in course_response:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Invalid course ID.')
                    }
                
                # Check if the course is already in the user's schedule
                user_courses = user_courses_table.get_item(Key={'user_id': drop_user_id})
                if 'Item' in user_courses:
                    courses_list = user_courses['Item'].get('courses', [])
                    if drop_course_id in courses_list:
                        courses_list.remove(drop_course_id)
                        user_courses_table.update_item(
                            Key={'user_id': drop_user_id},
                            UpdateExpression='SET courses = :val',
                            ExpressionAttributeValues={':val': courses_list}
                        )
                        return {
                            'statusCode': 200,
                            'body': json.dumps(f'Course {drop_course_id} dropped from {drop_user_id}\'s schedule.')
                        }
                    else:
                        return {
                            'statusCode': 400,
                            'body': json.dumps(f'Course {drop_course_id} is not in {drop_user_id}\'s schedule.')
                        }
                else:
                    return {
                        'statusCode': 400,
                        'body': json.dumps(f'No schedule found for {drop_user_id}.')
                    }
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps(f'Error: {str(e)}')
                }
