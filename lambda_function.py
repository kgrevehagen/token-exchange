import json
import requests
import os

def lambda_handler(event, context):
    authorization_code = event['queryStringParameters']['code']
    client_id = event['queryStringParameters']['client_id']
    code_verifier = event['queryStringParameters']['code_verifier']
    redirect_uri = event['queryStringParameters']['redirect_uri']

    token_endpoint = os.environ['TOKEN_ENDPOINT']

    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'client_id': client_id,
        'code_verifier': code_verifier,
        'redirect_uri': redirect_uri
    }

    response = requests.post(token_endpoint, data=data)

    return {
        'statusCode': response.status_code,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response.json())
    }
