from flask import Blueprint, request, jsonify
from app import db
from app.models import User, File

ops_blueprint = Blueprint("ops", __name__)

@ops_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]) and user.is_ops_user:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@ops_blueprint.route("/upload", methods=["POST"])
def upload_file():
    # Logic for file validation and saving will go here
    return jsonify({"message": "File uploaded successfully"}), 201
