from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.routes.ops_routes import ops_blueprint
    from app.routes.client_routes import client_blueprint
    app.register_blueprint(ops_blueprint, url_prefix="/ops")
    app.register_blueprint(client_blueprint, url_prefix="/client")

    return app
