from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.orders import bp
from app.models import Order, OrderItem
from app import db

@bp.route('/list')
@login_required
def list():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('orders/list.html', orders=orders)

@bp.route('/<int:id>')
@login_required
def view(id):
    order = Order.query.get_or_404(id)
    if order.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to view this order.', 'danger')
        return redirect(url_for('orders.list'))
    return render_template('orders/view.html', order=order) 