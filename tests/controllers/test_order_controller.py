import sys
sys.path.append('../../app')
import pytest
from unittest.mock import patch
from flask import json
from app.app import app
from app.controllers.order_controller import GetQuote, CreateOrder
from app.services.order_service import OrderService

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_order_service():
    with patch('app.controllers.OrderService') as mock_service:
        yield mock_service.return_value

def test_get_quote(client, mock_order_service):
    mock_order_service.get_quote.return_value = 50
    data = json.dumps({'product_id': 1, 'quantity': 2})
    response = client.post('/quote', data=data)
    assert response.status_code == 200
    assert response.json == {'price': 50, 'quantity': 2, 'total_cost': 100}

def test_create_order(client, mock_order_service):
    mock_order_service.create_order.return_value = 123
    data = json.dumps({'product_id': 1, 'quantity': 2})  # Replace with actual order data
    response = client.post('/orders', data=data)
    assert response.status_code == 200
    assert response.json == {'order_id': 123}
