from flask import request, jsonify
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.app import api
from app.services.user_service import UserService, get_db, close_db
from app.controllers.parsers import signup_parser, login_parser

user_service = UserService()

@api.route('/signup')
class Signup(Resource):

    @api.expect(signup_parser)
    def post(self):
        """
        Get a price quote for a product.
        """
        session = get_db()
        data = api.payload
        user_id = user_service.create_user(data, session)
        return jsonify({'user_id': user_id})

@api.route('/login')
class Login(Resource):

    @api.expect(login_parser)
    def post(self):
        """
        Submit an order to purchase a product.
        """
        data = api.payload
        session = get_db()
        access_token = user_service.login_user(data, session)
        return access_token

