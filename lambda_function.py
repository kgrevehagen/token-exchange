import json
import requests
import os


def lambda_handler(event, context):
    try:
        required_params = ["code", "client_id", "code_verifier", "redirect_uri"]
        query_params = event.get("queryStringParameters", {})

        missing_params = [
            param for param in required_params if param not in query_params
        ]
        if missing_params:
            return create_response(
                400, {"error": "Missing required parameters", "missing": missing_params}
            )

        params = {key: query_params[key] for key in required_params}

        token_endpoint = os.environ.get("TOKEN_ENDPOINT")
        if not token_endpoint:
            return create_response(
                500, {"error": "Missing TOKEN_ENDPOINT configuration"}
            )

        response = requests.post(
            token_endpoint, data={"grant_type": "authorization_code", **params}
        )

        if response.status_code == 200:
            return create_response(200, response.json())

        return create_response(
            response.status_code,
            {
                "error": "Failed to exchange authorization code",
                "details": response.json(),
            },
        )

    except Exception as e:
        return create_response(
            500, {"error": "Internal Server Error", "details": str(e)}
        )


def create_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body),
    }
