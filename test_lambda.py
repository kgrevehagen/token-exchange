import pytest
import json
from unittest.mock import patch
from lambda_function import lambda_handler

@pytest.fixture
def set_env(monkeypatch):
    monkeypatch.setenv("CLIENT_ID", "test-client-id")
    monkeypatch.setenv("CLIENT_SECRET", "test-client-secret")
    monkeypatch.setenv("TOKEN_ENDPOINT", "https://auth.example.com/oauth2/token")
    monkeypatch.setenv("REDIRECT_URI", "https://example.com/callback")

@patch("requests.post")
def test_invalid_code(mock_post, set_env):
    mock_post.return_value.status_code = 400
    mock_post.return_value.json.return_value = {"error": "invalid_grant"}

    event = {"queryStringParameters": {"code": "invalid_code"}}
    response = lambda_handler(event, None)
    
    body = json.loads(response['body'])
    
    assert response["statusCode"] == 400
    assert "invalid_grant" in body["error"]

@patch("requests.post")
def test_successful_token_exchange(mock_post, set_env):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"access_token": "test-access-token"}

    event = {"queryStringParameters": {"code": "valid_code"}}
    response = lambda_handler(event, None)

    body = json.loads(response['body'])

    assert response['statusCode'] == 200
    assert 'test-access-token' in body['access_token']