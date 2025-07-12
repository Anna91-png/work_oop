import pytest
from src.product import Product
from src.category import Category

def test_product_price_setter_positive():
    product = Product("Test", "desc", 100, 1)
    product.price = 200
    assert product.price == 200

def test_product_price_setter_negative(capsys):
    product = Product("Test", "desc", 100, 1)
    product.price = -10
    captured = capsys.readouterr()
    assert product.price == 100
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

def test_product_price_setter_zero(capsys):
    product = Product("Test", "desc", 100, 1)
    product.price = 0
    captured = capsys.readouterr()
    assert product.price == 100
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

def test_product_new_product():
    data = {"name": "Test", "description": "desc", "price": 500, "quantity": 4}
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Test"
    assert product.description == "desc"
    assert product.price == 500
    assert product.quantity == 4

def test_category_add_product_type_error():
    cat = Category("cat", "desc", [])
    with pytest.raises(TypeError):
        cat.add_product("not a product")

