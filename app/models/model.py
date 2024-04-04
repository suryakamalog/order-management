from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()

class User(Base, SerializerMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String)
    orders = relationship("Order", backref="order")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(Base, SerializerMixin):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    details = Column(String)
    quantity_available = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    user_id = Column(String, ForeignKey('user.id'))
    price = Column(Float)
    status = Column(String)

engine = create_engine('sqlite:///order_management.db')  # Connect to SQLite database
Base.metadata.create_all(engine)  # Create tables if they don't exist

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
