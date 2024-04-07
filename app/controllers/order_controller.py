from flask import request, jsonify
from app.app import api
from flask_restx import Resource
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.services.order_service import OrderService, get_db, close_db
from app.tasks import process_order_task

order_service = OrderService()

@api.route('/quote')
class GetQuote(Resource):

    def post(self):
        """
        Get a price quote for a product.
        """
        verify_jwt_in_request()
        product_id = api.payload['product_id']
        quantity = int(api.payload['quantity'])
        session = get_db()
        price = order_service.get_quote(product_id, session)
        return jsonify({'price': price, 'quantity': quantity, 'total_cost': price * quantity})

@api.route('/orders')
class CreateOrder(Resource):

    def post(self):
        """
        Submit an order to purchase a product.
        """
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        data = api.payload
        session = get_db()
        order_id = order_service.create_order(current_user, data, session)
        task_result = process_order_task.delay(data={"order_id": order_id})
        print(f"inside /product {task_result}")
        return jsonify({'order_id': order_id})

