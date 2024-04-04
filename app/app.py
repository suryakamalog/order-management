from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_migrate import Migrate
from datetime import timedelta
from celery import Celery

import json

app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///order_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Recommended for performance

db = SQLAlchemy(app)
migrate = Migrate(app, db)

celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
celery_app.conf.update({
    'CELERY_CONCURRENCY': 2,  # Adjust concurrency as needed
})

from app.controllers.order_controller import *
from app.controllers.product_controller import *
from app.controllers.user_controller import *

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5001/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Order Management"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('./swagger.json', 'r') as f:
        return jsonify(json.load(f))

