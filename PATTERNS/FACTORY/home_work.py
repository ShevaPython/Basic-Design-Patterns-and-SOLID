"""
Реализуйте систему управления заказами в интернет-магазине с помощью фабрики. Создайте классы для различных типов товаров
(например, электроника, одежда, книги) и классы для обработки заказов. Фабрика должна предоставлять методы для
создания экземпляров товаров на основе выбранного типа.
"""
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class Shopping(ABC):
    @abstractmethod
    def order(self):
        pass


class Electronic(Shopping):
    def __init__(self, gadget=None):
        self.gadget = gadget

    def order(self):
        print(F'Electronic order {self.gadget}')


class Garment(Shopping):
    def __init__(self,thin=None):
        self.thin = thin

    def order(self):
        print(F'Garment order: {self.thin}')


class Book(Shopping):
    def __init__(self, title=None):
        self.title = title

    def order(self):
        print(f'Book order: {self.title}')


class FactoryStore:
    @staticmethod
    def create_electronic(gadget):
        return Electronic(gadget)

    @staticmethod
    def create_garment(thin):
        return Garment(thin)

    @staticmethod
    def create_book(title):
        return Book(title)


factory = FactoryStore()
book = factory.create_book('Harry Potter')
book.order()
gadget = factory.create_electronic('Phone')
gadget.order()
thin = factory.create_garment('Chosen')
thin.order()