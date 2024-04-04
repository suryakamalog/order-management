from app.models.model import User, SessionLocal
from flask_jwt_extended import create_access_token
from flask import jsonify, make_response
class UserService:

    def create_user(self, data, db):
        user = User(first_name=data['first_name'], last_name=data['last_name'], username=data['username'], password_hash=data['password'])
        user.set_password(data['password'])
        db.add(user)
        db.commit()
        return user.id
        
    def login_user(self, data, db):
        username = data['username']
        password = data['password']
        # user = User.query.filter_by(username=username).first()
        user = db.query(User).filter_by(username=username).first()
        if user and user.verify_password(password):
            access_token = create_access_token(identity=username)
            return jsonify({'access_token': access_token})
        else:
            return make_response(jsonify({'message': 'Invalid username or password'}), 401)

def get_db():
    db = SessionLocal()
    return db

def close_db(db):
    db.close()
