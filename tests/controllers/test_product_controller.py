import pytest
from unittest.mock import patch
from flask import json

from app.app import app  # Import the app instance
from app.services.product_service import ProductService


@pytest.fixture()
def client():
    """Creates a test client with the app configured for testing."""
    with app.test_client() as client:
        with app.app_context():  # Ensure app context is active
            yield client


def test_get_all_products_success(client):
    """Tests successful retrieval of all products."""
    with patch('app.controllers.product_controller.verify_jwt_in_request') as jwt_mock:
        jwt_mock.return_value = True
        response = client.get('/product')

        assert response.status_code == 200


def test_create_product_success(client):
    """Tests successful product creation."""
    with patch('app.controllers.product_controller.verify_jwt_in_request') as jwt_mock:
        with patch('app.services.product_service.ProductService.create_product') as create_product_mock:
            jwt_mock.return_value = True  # Set mock return value for get_quote
            create_product_mock.return_value = 1
            payload = json.dumps({'price': 30, 'details': 'new product', 'quantity_available': 100})
            response = client.post('/product', data=payload, content_type='application/json')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['product_id'] == 1 # Assert returned product ID

