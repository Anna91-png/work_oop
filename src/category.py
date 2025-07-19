from typing import List
from src.product import Product


class Category:
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product] = None) -> None:
        self.name = name
        self.description = description
        self._products = products if products is not None else []

    def add_product(self, product: Product) -> None:
        print(f"Тип объекта: {type(product)}; Product класс: {Product}; isinstance: {isinstance(product, Product)}")
        if not isinstance(product, Product):
            raise TypeError("Only products can be added to the category")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        return self._products

    @property
    def total_product_count(self) -> int:
        return Category.product_count

    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."