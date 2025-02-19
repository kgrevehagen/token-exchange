# Token Exchange

This project is a small and simple function that exchanges an oauth2 authorization code for an oauth2 token.

## Setup

Run the `setup.sh` to get started. This will create and activate a virtual environment and install dependencies in it.

## Usage

To run it locally, fill in your configuration in `run.py` and run it:
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
- CLIENT_ID
- CLIENT_SECRET
- TOKEN_ENDPOINT
- REDIRECT_URI
3. Hook up some trigger to call your function, e.g. API Gateway.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
