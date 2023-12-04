import json
import boto3
from decimal import Decimal

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

                    # Check if the user is already in the maximum number of courses (6)
                    if len(courses_list) >= 6:
                        return {
                            'statusCode': 400,
                            'body': json.dumps(f'{user_id} is already in the maximum number of courses (6).')
                        }

                    if course_id in courses_list:
                        return {
                            'statusCode': 400,
                            'body': json.dumps(f'Course {course_id} is already added to {user_id}\'s schedule.')
                        }
                    else:
                        # Check if total_seats is equal to taken_seats
                        if 'taken_seats' in course_response['Item'] and 'total_seats' in course_response['Item']:
                            taken_seats = Decimal(course_response['Item']['taken_seats'])
                            total_seats = Decimal(course_response['Item']['total_seats'])
                            if taken_seats >= total_seats:
                                return {
                                    'statusCode': 400,
                                    'body': json.dumps(f'The course {course_id} is full. Cannot add to {user_id}\'s schedule.')
                                }
                    
                        # Update the taken_seats for the course by adding 1
                        update_expression = 'SET taken_seats = if_not_exists(taken_seats, :zero) + :val'
                        expression_attribute_values = {':val': 1, ':zero': Decimal('0')}
                        courses_table.update_item(
                            Key={'course_id': course_id},
                            UpdateExpression=update_expression,
                            ExpressionAttributeValues=expression_attribute_values
                        )

                        # Retrieve the updated course information after the update
                        updated_course = courses_table.get_item(Key={'course_id': course_id})['Item']
                        if 'taken_seats' in updated_course and 'total_seats' in updated_course:
                            taken_seats = Decimal(updated_course['taken_seats'])
                            total_seats = Decimal(updated_course['total_seats'])
                            if taken_seats >= total_seats:
                                # Rollback the update if the course is now full
                                courses_table.update_item(
                                    Key={'course_id': course_id},
                                    UpdateExpression='SET taken_seats = :val',
                                    ExpressionAttributeValues={':val': taken_seats - 1}
                                )
                                return {
                                    'statusCode': 400,
                                    'body': json.dumps(f'The course {course_id} is full. Cannot add to {user_id}\'s schedule.')
                                }

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