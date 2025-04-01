from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app.main import bp
from app.models import Product
from app import db

@bp.route('/')
@bp.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=12)
    return render_template('index.html', products=products)

@bp.route('/product/<int:id>')
def product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)

@bp.route('/category/<category>')
def category(category):
    page = request.args.get('page', 1, type=int)
    products = Product.query.filter_by(category=category).paginate(page=page, per_page=12)
    return render_template('category.html', products=products, category=category) 