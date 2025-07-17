from src.BaseProduct import BaseProduct
from src.InfoMixin import InfoMixin

class Product(InfoMixin, BaseProduct):
    product_count = 0

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        Product.product_count += 1

    @classmethod
    def new_product(cls, prod_dict):
        return cls(
            prod_dict["name"],
            prod_dict["description"],
            prod_dict["price"],
            prod_dict["quantity"]
        )

    def get_info(self) -> str:
        return f"{self.name} - {self.description} ({self.price} руб., {self.quantity} шт.)"

    def __str__(self) -> str:
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Cannot add products of different types")
        return self.price + other.price