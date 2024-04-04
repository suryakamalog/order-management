from app.models.model import User, Product, Order, SessionLocal

class OrderService:

    def get_quote(self, product_id, db):
        product = db.query(Product).get(product_id)
        price = product.price
        return float(price)  # Return price of the requested product

    def create_order(self, username, data, db):
        current_user_id = db.query(User).filter_by(username=username).first().id
        order = Order(product_id=data['product_id'], user_id=current_user_id, price=self.get_quote(data['product_id'], db))
        db.add(order)
        db.commit()
        return order.id  # Return the order ID

def get_db():
    db = SessionLocal()
    return db

def close_db(db):
    db.close()
