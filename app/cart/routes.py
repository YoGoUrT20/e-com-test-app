from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.cart import bp
from app.models import Product, Order, OrderItem
from app import db

@bp.route('/view')
@login_required
def view():
    return render_template('cart/view.html')

@bp.route('/add', methods=['POST'])
@login_required
def add():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = int(data.get('quantity', 1))
    
    product = Product.query.get_or_404(product_id)
    
    if product.stock < quantity:
        return jsonify({
            'success': False,
            'message': 'Not enough stock available'
        })
    
    # Here you would typically add the item to the user's cart
    # For now, we'll just return success
    return jsonify({
        'success': True,
        'message': 'Product added to cart'
    })

@bp.route('/checkout')
@login_required
def checkout():
    return render_template('cart/checkout.html') 