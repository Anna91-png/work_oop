from src.BaseProduct import BaseProduct
from src.InfoMixin import InfoMixin


class Product(InfoMixin, BaseProduct):
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self._price = None
        self.name = name
        self.description = description
        self.price = price  # работает через сеттер
        self.quantity = quantity
        Product.product_count += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def get_info(self) -> str:
        return f"{self.name} - {self.description} ({self.price} руб., {self.quantity} шт.)"

    def __str__(self) -> str:
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только продукты одного типа")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, prod_dict):
        return cls(
            prod_dict["name"],
            prod_dict["description"],
            prod_dict["price"],
            prod_dict["quantity"]
        )