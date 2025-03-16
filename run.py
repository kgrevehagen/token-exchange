import os
from lambda_function import lambda_handler

# Fill in your configuration
os.environ['TOKEN_ENDPOINT'] = 'your_token_endpoint'
authorization_code = 'your_authorization_code'
client_id = 'your_client_id'
code_verifier = 'your_code_verifier'
redirect_uri = 'your_redirect_uri'

event = {
    'queryStringParameters': {
        'code': authorization_code,
        'client_id': client_id,
        'code_verifier': code_verifier,
        'redirect_uri': redirect_uri
    }
}

response = lambda_handler(event, None)

print(response)