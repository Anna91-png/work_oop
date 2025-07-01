from .product import Product

class Category:
    product_count = 0  # Класс-переменная для общего количества товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            self.add_product(product)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект класса Product")
        self.__products.append(product)
        Category.product_count += 1  # Работает, так как product_count — это переменная класса

    @property
    def products(self):
        result = ""
        for prod in self.__products:
            result += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return result.rstrip('\n')

    @property
    def total_product_count(self):
        return Category.product_count