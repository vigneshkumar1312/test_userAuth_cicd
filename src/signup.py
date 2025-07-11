import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('test-vk-users')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    email = data['email']
    password = data['password']

    table.put_item(Item={
        'userId': str(uuid.uuid4()),
        'email': email,
        'password': password  # Hash it in real apps!
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'User signed up successfully'})
    }
