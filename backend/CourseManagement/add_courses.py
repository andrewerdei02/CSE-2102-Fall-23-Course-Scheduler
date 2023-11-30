# lambda function for adding courses to a users schedule
import boto3
import json

dynamodb = boto3.resource('dynamodb')
user_courses_table = dynamodb.Table('UserCourses')

def lambda_handler(event, context):
    user_id = event['user_id']
    course_id = event['course_id']
    
    user_courses = user_courses_table.get_item(Key={'user_id': user_id})
    if 'Item' in user_courses:
        # user exists in the table
        courses = user_courses['Item'].get('courses', [])
        if course_id in courses:
            return {
                'statusCode': 400,
                'body': json.dumps('Course already added!')
            }
        courses.append(course_id)
        user_courses_table.update_item(
            Key={'user_id': user_id},
            UpdateExpression='SET courses = :c',
            ExpressionAttributeValues={':c': courses}
        )
    else:
        # user doesn't exist, create a new entry with an empty list of courses
        user_courses_table.put_item(
            Item={'user_id': user_id, 'courses': [course_id]}
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Course added successfully!')
    }
