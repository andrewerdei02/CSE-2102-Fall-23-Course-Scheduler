# lambda function for dropping user courses
import boto3
import json

dynamodb = boto3.resource('dynamodb')
user_courses_table = dynamodb.Table('UserCourses')

def lambda_handler(event, context):
    user_id = event['user_id']
    course_id = event['course_id']
    
    user_courses = user_courses_table.get_item(Key={'user_id': user_id})
    if 'Item' in user_courses:
        courses = user_courses['Item'].get('courses', [])
        if course_id in courses:
            courses.remove(course_id)
            user_courses_table.update_item(
                Key={'user_id': user_id},
                UpdateExpression='SET courses = :c',
                ExpressionAttributeValues={':c': courses}
            )
            return {
                'statusCode': 200,
                'body': json.dumps('Course dropped successfully!')
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Course not found for this user!')
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('User not found!')
        }

