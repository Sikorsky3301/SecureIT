from app.models import User

def test_ops_login(client):
    # Create an Ops User in the test DB
    user = User(username="ops_user", is_ops_user=True)
    user.set_password("password123")
    db.session.add(user)
    db.session.commit()

    # Test the /ops/login endpoint
    response = client.post("/ops/login", json={"username": "ops_user", "password": "password123"})
    assert response.status_code == 200
    assert response.get_json()["message"] == "Login successful"
