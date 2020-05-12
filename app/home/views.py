from flask import jsonify
from datetime import date
import jsonpickle
from . import home
from ..schema import *
from .query import *


@home.route('/')
def homepage():
    return "This is an Ecommerce API"
    
@home.route('/products')
def GetProducts():
    products = Product.query.all()
    schema = ProductSchema(many=True)
    result=schema.dumps(products)
    return result

@home.route('/product/<int:p_id>')
def ProductDetails(p_id):
    product = Product.query.filter_by(productid = p_id).first()
    schema = ProductSchema()
    results = schema.dumps(product)
    return results

@home.route('/categories')
def GetCategories():
    categories = Category.query.all()
    schema = CategorySchema(many=True)
    results = schema.dumps(categories)     
    return results

@home.route('/categories/<int:cat_id>')
def GetCategory(cat_id):
    category = ProductCategory.query.filter_by(categoryid = cat_id).all()
    schema = ProductCategorySchema(many=True)
    results = schema.dumps(category)     
    return results

@home.route('/productcategories/<int:pc_id>/products')
def CategoryProducts(pc_id):
    products = Product.query.filter_by(productcategoryid = pc_id).all()
    schema = ProductSchema(many=True)
    result=schema.dumps(products)
    return result