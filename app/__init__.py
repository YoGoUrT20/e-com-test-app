from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    from app.admin import admin as admin_blueprint
    from app.products import products as products_blueprint
    from app.cart import cart as cart_blueprint
    from app.orders import orders as orders_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(products_blueprint, url_prefix='/products')
    app.register_blueprint(cart_blueprint, url_prefix='/cart')
    app.register_blueprint(orders_blueprint, url_prefix='/orders')

    return app 