def test_client_signup(client):
    response = client.post("/client/signup", json={
        "username": "client_user",
        "email": "client@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 201
    assert "encrypted_url" in response.get_json()
    assert response.get_json()["message"] == "User created successfully"
