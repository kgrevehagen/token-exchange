import pytest
import json
from unittest.mock import patch
from lambda_function import lambda_handler


@pytest.fixture
def set_env(monkeypatch):
    monkeypatch.setenv("TOKEN_ENDPOINT", "https://auth.example.com/oauth2/token")


def test_missing_params():
    event = {
        "queryStringParameters": {
            "client_id": "client_id",
            "code_verifier": "code_verifier",
        }
    }
    response = lambda_handler(event, None)

    body = json.loads(response["body"])

    assert response["statusCode"] == 400
    assert response["headers"]["Access-Control-Allow-Origin"] == "*"
    assert set(body["missing"]) == {"code", "redirect_uri"}


@patch("requests.post")
def test_invalid_code(mock_post, set_env):
    mock_post.return_value.status_code = 400
    mock_post.return_value.json.return_value = {"error": "invalid_grant"}

    event = {
        "queryStringParameters": {
            "code": "invalid_code",
            "client_id": "client_id",
            "code_verifier": "code_verifier",
            "redirect_uri": "redirect_uri",
        }
    }
    response = lambda_handler(event, None)

    body = json.loads(response["body"])

    assert response["statusCode"] == 400
    assert response["headers"]["Access-Control-Allow-Origin"] == "*"
    assert "invalid_grant" in body["details"]["error"]


@patch("requests.post")
def test_successful_token_exchange(mock_post, set_env):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"access_token": "test-access-token"}

    event = {
        "queryStringParameters": {
            "code": "valid_code",
            "client_id": "client_id",
            "code_verifier": "code_verifier",
            "redirect_uri": "redirect_uri",
        }
    }
    response = lambda_handler(event, None)

    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert response["headers"]["Access-Control-Allow-Origin"] == "*"
    assert "test-access-token" in body["access_token"]
