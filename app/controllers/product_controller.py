from flask import request, jsonify
from flask_restx import Resource
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from app.app import api
from app.services.product_service import ProductService, get_db, close_db

product_service = ProductService()

@api.route('/product')
class GetProduct(Resource):
    def get(self):
        """
        Get a price quote for a product.
        """
        session = get_db()
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        products = product_service.get_all_product(session)
        return jsonify({'products': products})

    def post(self):
        """
        Submit an order to purchase a product.
        """
        data = api.payload
        session = get_db()
        verify_jwt_in_request()
        product_id = product_service.create_product(data, session)
        return jsonify({'product_id': product_id})

