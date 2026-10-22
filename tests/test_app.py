from app import get_products


def test_products_available():
    products = get_products()
    assert len(products) > 0


def test_product_has_required_fields():
    for product in get_products():
        assert "id" in product
        assert "name" in product
        assert "price" in product


def test_product_prices_are_positive():
    for product in get_products():
        assert product["price"] > 0