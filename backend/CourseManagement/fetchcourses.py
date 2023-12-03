# function to fetch all available courses
import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
courses_table = dynamodb.Table('Courses')

# Function to handle Decimal serialization for JSON conversion
def convert_decimal(obj):
    if isinstance(obj, Decimal):
        if obj % 1 == 0:
            return int(obj)
        else:
            return float(obj)
    raise TypeError

def lambda_handler(event, context):
    response = courses_table.scan()
    courses = response['Items']
    
    # Convert Decimal types to float or int for JSON serialization
    courses_serializable = json.loads(json.dumps(courses, default=convert_decimal))
    
    return {
        'statusCode': 200,
        'body': json.dumps(courses_serializable)
    }
