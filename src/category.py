from product import Product

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
        return self.__products  # Return the actual list of products

    @property
    def total_product_count(self):
        return Category.product_count

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории с общим количеством товаров.
        """
        total_quantity = sum(product.quantity for product in self.__products)  # Use __products
        return f"{self.name}, количество продуктов: {total_quantity} шт."

