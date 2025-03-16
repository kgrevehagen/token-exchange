# Token Exchange

This project is a small and simple function that exchanges an oauth2 authorization code for an oauth2 token.

## Setup

Run the `setup.sh` to get started. This will create and activate a virtual environment and install dependencies in it.

## Usage

To run it locally, fill in your configuration/query parameters in `run.py` and run it:
```sh
python run.py
```

## Tests

To run the tests:
```sh
pytest test_lambda.py
```

## Packaging

1. Run the `package.sh` to get a packaged .zip file.

## How to use in AWS Lambda

1. Import the .zip file to your AWS Lambda function.
2. Set the following environment variables in your configuration in AWS Lambda:
- TOKEN_ENDPOINT
3. Hook up some trigger to call your function, e.g. API Gateway.

## Usage
Add the following query parameters to the request:

`code`: The authorization code received from the authorize endpoint.

`client_id`: The client id of the app client, similar to the one used in the authorization endpoint.

`code_verifier`: The code verifier generated when calling the authorization endpoint.

`redirect_uri`: The same redirect uri as for the authorization endpoint.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
