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

    def test_product_zero_quantity_raises_valueerror():
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Тест", "описание", 100, 0)

    def test_middle_price_correct():
        product1 = Product("Test1", "desc1", 100.0, 1)
        product2 = Product("Test2", "desc2", 200.0, 2)
        category = Category("Категория", "Описание", [product1, product2])
        assert category.middle_price() == 150.0

    def test_middle_price_empty_category():
        category = Category("Пустая", "Без продуктов", [])
        assert category.middle_price() == 0