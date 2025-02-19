import json
import requests
import os

def lambda_handler(event, context):
    authorization_code = event['queryStringParameters']['code']

    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    token_endpoint = os.environ['TOKEN_ENDPOINT']
    redirect_uri = os.environ['REDIRECT_URI']
    
    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }

    response = requests.post(token_endpoint, data=data)

    return {
        'statusCode': response.status_code,
        'body': json.dumps(response.json())
    }
