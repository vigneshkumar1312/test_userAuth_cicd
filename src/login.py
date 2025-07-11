import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    email = data['email']
    password = data['password']

    response = table.scan(
        FilterExpression="email = :e and password = :p",
        ExpressionAttributeValues={':e': email, ':p': password}
    )

    if response['Items']:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Login successful'})
        }
    else:
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Invalid credentials'})
        }
