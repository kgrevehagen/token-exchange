import os
from lambda_function import lambda_handler

# Fill in your configuration
os.environ['CLIENT_ID'] = 'your_client_id'
os.environ['CLIENT_SECRET'] = 'your_client_secret'
os.environ['TOKEN_ENDPOINT'] = 'your_token_endpoint'
os.environ['REDIRECT_URI'] = 'your_redirect_uri'
authorization_code = 'your_authorization_code'

event = {
    'queryStringParameters': {
        'code': authorization_code
    }
}

response = lambda_handler(event, None)

print(response)