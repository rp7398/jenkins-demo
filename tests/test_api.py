from app.main import create_app

def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "UP"

def test_add():
    app = create_app()
    client = app.test_client()

    response = client.get("/add/2/3")
    assert response.json["result"] == 5
