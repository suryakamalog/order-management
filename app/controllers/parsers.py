from flask_restx import reqparse
from app.app import api

signup_parser = api.parser()
signup_parser.add_argument('first_name', location='json', required=True)
signup_parser.add_argument('last_name', location='json', required=True)
signup_parser.add_argument('username', location='json', required=True)
signup_parser.add_argument('password', location='json', required=True)

login_parser = api.parser()
login_parser.add_argument('username', location='json', required=True)
login_parser.add_argument('password', location='json', required=True)

quote_parser = api.parser()
quote_parser.add_argument('Authorization', location='headers', required=True, help='<token>')
quote_parser.add_argument('product_id', location='json', required=True)
quote_parser.add_argument('quantity', location='json', required=True, type=int)

order_parser = api.parser()
order_parser.add_argument('Authorization', location='headers', required=True, help='<token>')
order_parser.add_argument('product_id', location='json', required=True)
order_parser.add_argument('price', location='json', required=True, type=int)

product_parser = api.parser()
product_parser.add_argument('Authorization', location='headers', required=True, help='<token>')
product_parser.add_argument('price', location='json', required=True, type=float)
product_parser.add_argument('details', location='json', required=True)
product_parser.add_argument('quantity_available', location='json', required=True, type=int)