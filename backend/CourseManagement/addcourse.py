# function for students to add a course to their schedule
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
            # Get data from the API request
            try:
                body = json.loads(event['body'])
                user_id = body.get('user_id')
                course_id = body.get('course_id')
        
                # Check if user_id or course_id is missing
                if not user_id or not course_id:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Please provide both username and course_id.')
                    }
        
                # Check if the user exists in UserData table
                user_response = user_data_table.get_item(Key={'username': user_id})
                if 'Item' not in user_response:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Invalid username.')
                    }
        
                # Check if the course exists in Courses table
                course_response = courses_table.get_item(Key={'course_id': course_id})
                if 'Item' not in course_response:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Invalid course ID.')
                    }
        
                # Check if the course is already added to the user's courses
                user_courses = user_courses_table.get_item(Key={'user_id': user_id})
                if 'Item' in user_courses:
                    courses_list = user_courses['Item'].get('courses', [])
                    if course_id in courses_list:
                        return {
                            'statusCode': 400,
                            'body': json.dumps(f'Course {course_id} is already added to {user_id}\'s schedule.')
                        }
                    else:
                        courses_list.append(course_id)
                        user_courses_table.update_item(
                            Key={'user_id': user_id},
                            UpdateExpression='SET courses = :val',
                            ExpressionAttributeValues={':val': courses_list}
                        )
                else:
                    user_courses_table.put_item(Item={'user_id': user_id, 'courses': [course_id]})
        
                return {
                    'statusCode': 201,
                    'body': json.dumps(f'Course {course_id} added to {user_id}\'s schedule successfully.')
                }
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps(f'Error: {str(e)}')
                }
