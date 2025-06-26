import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.shop import  Product, Category

def test_product_initialization():
    p = Product("Телефон", "Смартфон с камерой", 19999.90, 15)
    assert p.name == "Телефон"
    assert p.description == "Смартфон с камерой"
    assert p.price == 19999.90
    assert p.quantity == 15

def test_category_initialization_and_class_attributes():
    # Сбросим счетчики для теста
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Ноутбук", "Игровой ноутбук", 89999.99, 5)
    p2 = Product("Мышь", "Беспроводная мышь", 1200.00, 25)

    category1 = Category("Электроника", "Различные электронные товары", [p1, p2])
    assert category1.name == "Электроника"
    assert category1.description == "Различные электронные товары"
    assert category1.products == [p1, p2]
    assert Category.category_count == 1
    assert Category.product_count == 2

    p3 = Product("Книга", "Роман", 500.00, 50)
    category2 = Category("Книги", "Художественная литература", [p3])
    assert Category.category_count == 2
    assert Category.product_count == 3

def test_category_product_list():
    p1 = Product("Чайник", "Электрический чайник", 2500.00, 10)
    p2 = Product("Тостер", "Двухсекционный тостер", 1800.00, 7)
    cat = Category("Бытовая техника", "Техника для дома", [p1, p2])
    assert len(cat.products) == 2
    assert all(isinstance(prod, Product) for prod in cat.products)