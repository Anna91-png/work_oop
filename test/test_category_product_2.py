import pytest
from src.product import Product
from src.category import Category

def test_product_str():
    product = Product("Test", "desc", 80, 15)
    assert str(product) == "Test, 80 руб. Остаток: 15 шт."

def test_category_str():
    p1 = Product("A", "desc", 10, 2)
    p2 = Product("B", "desc", 5, 3)
    cat = Category("Cat", "desc", [p1, p2])
    assert str(cat) == "Cat, количество продуктов: 5 шт."

def test_product_add():
    p1 = Product("A", "desc", 100, 10)
    p2 = Product("B", "desc", 200, 2)
    assert p1 + p2 == 100*10 + 200*2

def test_category_products_property():
    p1 = Product("A", "desc", 10, 2)
    cat = Category("Cat", "desc", [p1])
    assert cat.products == [p1]
    assert str(cat.products[0]) == "A, 10 руб. Остаток: 2 шт."