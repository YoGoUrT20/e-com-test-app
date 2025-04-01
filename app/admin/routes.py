from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.admin import bp
from app.models import Product, User, Order
from app import db
from functools import wraps

def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

@bp.route('/products')
@admin_required
def products():
    products = Product.query.all()
    return render_template('admin/products.html', products=products)

@bp.route('/orders')
@admin_required
def orders():
    orders = Order.query.all()
    return render_template('admin/orders.html', orders=orders)

@bp.route('/users')
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', users=users) 