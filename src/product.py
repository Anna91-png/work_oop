from typing import Any

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, prod_dict):
        return cls(
            prod_dict["name"],
            prod_dict["description"],
            prod_dict["price"],
            prod_dict["quantity"]
        )

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара.
        """
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """
        Складывает стоимость всех товаров на складе для двух объектов Product.
        """
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity