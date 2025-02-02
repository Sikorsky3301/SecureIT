from flask import Blueprint, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from datetime import datetime
from app import db, bcrypt
from app.models import User  # Corrected import for User model

# Assuming app and db are initialized elsewhere
client_blueprint = Blueprint("client", __name__)
serializer = URLSafeTimedSerializer("your_secret_key")

# Download model to track downloads
class Download(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    file_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@client_blueprint.route("/signup", methods=["POST"])
def signup():
    from app.models import User  # Import inside function to avoid circular import issues
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Username, email, and password are required"}), 400

    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return jsonify({"error": "Username or email already exists"}), 409

    new_user = User()
    new_user.username = username
    new_user.email = email
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@client_blueprint.route("/downloads/<int:user_id>", methods=["GET"])
def list_downloads(user_id):
    downloads = Download.query.filter_by(user_id=user_id).all()
    download_list = [
        {"file_id": d.file_id, "timestamp": d.timestamp.strftime("%Y-%m-%d %H:%M:%S")} 
        for d in downloads
    ]
    return jsonify(download_list), 200

# Helper function to generate secure download link
def generate_secure_link(file_id, user_id):
    token = serializer.dumps({"file_id": file_id, "user_id": user_id})
    return f"https://yourdomain.com/download/{token}"
