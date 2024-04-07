import pytest
from unittest.mock import patch
from flask import json

from app.app import app  # Import the app instance
from app.services.order_service import OrderService  # Import OrderService


@pytest.fixture()
def client():
    """Creates a test client with the app configured for testing."""
    with app.test_client() as client:
        with app.app_context():  # Ensure app context is active
            yield client


@pytest.fixture()
def mock_order_service():
    """Mocks the OrderService with desired behavior."""
    with patch('app.services.order_service') as mock:
        mock.get_quote.return_value = 10  # Set mock return value for get_quote
        yield mock

@pytest.fixture()
def mock_verify_jwt_in_request():
    with patch('app.controllers.order_controller.verify_jwt_in_request') as mock:
        mock.return_value = True  # Set mock return value for get_quote
        yield mock


def test_get_quote_success(client, mock_verify_jwt_in_request):
    """Tests a successful quote request with valid JWT."""
    with patch('flask_jwt_extended.verify_jwt_in_request'):  # Mock JWT verification
        payload = json.dumps({'product_id': 1, 'quantity': 2})
        response = client.post('/quote', data=payload, content_type='application/json')
        assert response.status_code == 200



def test_get_quote_missing_payload(client, mock_verify_jwt_in_request):
    """Tests handling a request with missing payload data."""
    with patch('flask_jwt_extended.verify_jwt_in_request'):  # Mock JWT verification
        response = client.post('/quote', content_type='application/json')

        assert response.status_code == 400  # Bad Request
