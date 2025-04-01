from flask import render_template
from app.products import products
from app.models import Product

@products.route('/')
def index():
    products = Product.query.all()
    return render_template('products/index.html', products=products) 