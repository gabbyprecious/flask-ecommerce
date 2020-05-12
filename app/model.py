from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    address = db.Column(db.String(50), unique=False, nullable=False)
    city = db.Column(db.String(20), unique=False, nullable=False)
    state = db.Column(db.String(20), unique=False, nullable=False)
    country = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.String(20), nullable=False)


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}'), " \
               f"'{self.address1}', '{self.city}', '{self.state}', '{self.country}'," \
               f"'{self.email}','{self.phone}')"

class Product(db.Model):
    __tablename__ = 'product'
    
    productid = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    productcategoryid =  db.Column(db.Integer, db.ForeignKey('product_category.product_categoryid'), nullable=False)
    price = db.Column(db.DECIMAL)    

    def __repr__(self):
        return f"Product('{self.productid}','{self.product_name}','{self.description}', '{self.quantity}', '{self.price}')"

class Category(db.Model):
    __tablename__ = 'category'
 
    categoryid = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Category('{self.categoryid}', '{self.category_name}')"
    
class ProductCategory(db.Model):
    __tablename__ = 'product_category'

    product_categoryid = db.Column(db.Integer, primary_key=True)
    product_categoryname = db.Column(db.String(100), nullable=False)
    categoryid = db.Column(db.Integer, db.ForeignKey('category.categoryid'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"ProductCategory('{self.categoryid}', '{self.product_categoryid}', '{self.product_categoryname}')"
    
class Cart(db.Model):
    __tablename__ = 'cart'
    
    cart_id = db.Column(db.Integer, primary_key=True, unique=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False, primary_key=True)
    productid = db.Column(db.Integer, db.ForeignKey('product.productid'), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Cart('{self.userid}', '{self.productid}, '{self.quantity}')"


class Order(db.Model):
    __tablename__ = 'order'
    
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'), nullable=False,)
    total_price = db.Column(db.DECIMAL, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False, primary_key=True)

    def __repr__(self):
        return f"Order('{self.orderid}', '{self.order_date}','{self.total_price}','{self.userid}'')"
