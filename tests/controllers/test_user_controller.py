import pytest
from unittest.mock import patch
from flask import json

from app.app import app  # Import the app instance
from app.services.user_service import UserService


@pytest.fixture()
def client():
    """Creates a test client with the app configured for testing."""
    with app.test_client() as client:
        with app.app_context():  # Ensure app context is active
            yield client


@pytest.fixture()
def mock_user_service():
    """Mocks the UserService with desired behavior."""
    with patch('app.services.user_service') as mock:
        mock.create_user.return_value = 1
        mock.login_user.return_value = 'access_token'
        yield mock


def test_signup_success(client, mock_user_service):
    """Tests successful user signup."""
    with patch('app.services.user_service.UserService.create_user') as create_user_mock:
        create_user_mock.return_value = 'dummy_user_id'
        payload = json.dumps({'first_name': 'dummy_first_name', 'last_name': 'dummy_last_name', 'username': 'testuser', 'password': 'testpassword'})
        response = client.post('/signup', data=payload, content_type='application/json')

        assert response.status_code == 200
        assert json.loads(response.data) == {'user_id': 'dummy_user_id'}


def test_login_success(client, mock_user_service):
    """Tests successful user login."""
    with patch('app.services.user_service.UserService.login_user') as login_mock:
        login_mock.return_value = {'access_token': 'dummy_access_token'}
        payload = json.dumps({'username': 'testuser', 'password': 'testpassword'})
        response = client.post('/login', data=payload, content_type='application/json')

        assert response.status_code == 200
        assert json.loads(response.data) == {'access_token': 'dummy_access_token'}  # Assert access token is returned


