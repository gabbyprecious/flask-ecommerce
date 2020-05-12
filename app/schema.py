from marshmallow import Schema, fields
from .model import *


class ProductSchema(Schema):
    productid = fields.Int()
    product_name = fields.Str()
    description = fields.Str()
    quantity = fields.Int()
    price = fields.Int()
    

class CategorySchema(Schema):
    categoryid = fields.Int()
    category_name = fields.Str()

class ProductCategorySchema(Schema):
    product_categoryid = fields.Int()
    product_categoryname = fields.Str()
    productid = fields.Int()