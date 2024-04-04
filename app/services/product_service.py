from app.models.model import Product, SessionLocal
from flask import jsonify
class ProductService:

    def create_product(self, data, db):
        product = Product(price=data['price'], details=data['details'], quantity_available=data['quantity_available'])
        db.add(product)
        db.commit()
        return product.id  # Return the product ID
    
    def get_all_product(self, db):
        products = db.query(Product).all()
        product_data = [p.to_dict() for p in products]
        return product_data  # Return all products

def get_db():
    db = SessionLocal()
    return db

def close_db(db):
    db.close()
