"""
OCP - принцип открытости и закрытости
Открытый для разшинения закрытый для модификации!
"""
from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(self, products, size):
        """
        Добавляем новый функционал фильтрации по size этим самым мы нарушаем принцип OSP ,потому-что при добавлении
        нового функционала мы должны добавлять ее через расширения а не через модификацию!
        """
        for product in products:
            if product.size == size:
                yield product

    def filter_by_size_and_color(self, products, size, color):
        for product in products:
            if product.size == size and product.color == color:
                yield product


# Specification

class Specification(ABC):
    """Создвем класс для определения нужного критерия"""

    @abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter(ABC):
    """Будут похож на класс высше но мы не будем добавлять в него функционал а с помощу наследника
    будем разширять его"""

    @abstractmethod
    def filter(self, items, specification: Specification):
        pass


class ColorSpecification(Specification):
    """Разширяем функционал"""

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    """Разширяем функционал"""

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    """Разширяем функционал для обработки фильтра filter_by_size_and_color"""

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item),
            self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, specification: Specification):
        for item in items:
            if specification.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.RED, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # old version
    prodfilter = ProductFilter()
    print('Green products (old version):')
    for product in prodfilter.filter_by_color(products, Color.GREEN):
        print(F"- {product.name} is green")

    # new version OSP
    betterfilter = BetterFilter()
    print('Green products (new version):')
    green = ColorSpecification(Color.GREEN)
    for product in betterfilter.filter(products, green):
        print(F"- {product.name} is green")

    print("Large products (new version):")
    large = SizeSpecification(Size.LARGE)
    for product in betterfilter.filter(products, large):
        print(F"- {product.name} is large")

    #filter_by_size_and_color new version
    print("Large and blue items (new version):")
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    large_blue = large & ColorSpecification(Color.BLUE)
    for p in betterfilter.filter(products, large_blue):
        print(f' - {p.name} is large and blue')
