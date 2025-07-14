from typing import List
from src.product import Product


class Category:
    product_count = 0  # Класс-переменная для общего количества товаров

    def __init__(self, name: str, description: str, products: List[Product] = None) -> None:
        self.name = name
        self.description = description
        self._products = products if products is not None else []  # Используем временный атрибут

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Only products can be added to the category")
        self._products.append(product)
        Category.product_count += 1  # Увеличиваем общее количество товаров

    @property
    def products(self) -> List[Product]:
        return self._products  # Возвращаем фактический список продуктов

    @products.setter
    def products(self, value: List[Product]) -> None:
        if not isinstance(value, list):
            raise TypeError("Products must be a list")
        self._products = value

    @property
    def total_product_count(self) -> int:
        return Category.product_count

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории с общим количеством товаров.
        """
        total_quantity = sum(product.quantity for product in self._products)  # Используем _products
        return f"{self.name}, количество продуктов: {total_quantity} шт."
