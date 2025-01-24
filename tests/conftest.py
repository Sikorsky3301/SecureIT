import pytest
from app import create_app, db

@pytest.fixture
def app():
    # Create the Flask app with a test configuration
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use in-memory database for testing
    with app.app_context():
        db.create_all()  # Initialize the test database
        yield app
        db.session.remove()
        db.drop_all()  # Clean up the database after tests

@pytest.fixture
def client(app):
    # Create a test client for sending requests to the app
    return app.test_client()
