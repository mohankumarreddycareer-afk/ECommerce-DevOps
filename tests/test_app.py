import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_home_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_products_available(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json) > 0


def test_product_has_required_fields(client):
    response = client.get("/products")

    for product in response.json:
        assert "id" in product
        assert "name" in product
        assert "price" in product


def test_product_prices_are_positive(client):
    response = client.get("/products")

    for product in response.json:
        assert product["price"] > 0


def test_get_single_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json["name"] == "Laptop"


def test_product_not_found(client):
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json["error"] == "Product not found"