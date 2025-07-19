import pytest
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass
from src.category import Category


def test_add_subclass_product():
    smartphone = Smartphone("iPhone", "desc", 100000, 3, 95.5, "15 Pro", 256, "gray")
    grass = LawnGrass("Газон", "Трава", 300, 10, "Россия", "7 дней", "зеленый")
    category = Category("Разное", "Смартфоны и трава", [])

    category.add_product(smartphone)
    category.add_product(grass)

    assert smartphone in category.products
    assert grass in category.products


def test_add_invalid_object_raises_typeerror():
    category = Category("Техника", "Разная техника", [])

    with pytest.raises(TypeError):
        category.add_product("я просто строка, не продукт")

    with pytest.raises(TypeError):
        category.add_product(12345)


def test_smartphone_initialization():
    phone = Smartphone("Xiaomi", "Redmi Note 12", 40000, 5, 88.5, "Note 12", 128, "синий")

    assert phone.name == "Xiaomi"
    assert phone.description == "Redmi Note 12"
    assert phone.price == 40000
    assert phone.quantity == 5
    assert phone.efficiency == 88.5
    assert phone.model == "Note 12"
    assert phone.memory == 128
    assert phone.color == "синий"


def test_lawngrass_initialization():
    grass = LawnGrass("Газон", "Красивая трава", 350.0, 10, "Германия", "6 дней", "темно-зеленый")

    assert grass.name == "Газон"
    assert grass.description == "Красивая трава"
    assert grass.price == 350.0
    assert grass.quantity == 10
    assert grass.country == "Германия"
    assert grass.germination_period == "6 дней"
    assert grass.color == "темно-зеленый"

    def test_smartphone_creation_prints_info(capfd):
        phone = Smartphone("iPhone", "Apple phone", 1000.0, 5, 90.5, "15 Pro", 256, "Black")
        captured = capfd.readouterr()
        assert "Создан объект класса Smartphone" in captured.out

    def test_lawngrass_creation_prints_info(capfd):
        grass = LawnGrass("Greeny", "For summer", 500.0, 2, "Russia", "Fast", "Summer")
        captured = capfd.readouterr()
        assert "Создан объект класса LawnGrass" in captured.out