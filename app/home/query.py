from ..model import *
from .. import db

def ProductDetails(ProductID):
    product = Product.query.filter_by(productid = ProductID).all()
    return product

def GetProducts():
    products = Product.query.all
    return products