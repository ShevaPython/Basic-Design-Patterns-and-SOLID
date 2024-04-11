"""
Prototype
Паттерн Прототип (Prototype) позволяет создавать новые объекты на основе уже существующих объектов-прототипов, избегая
дополнительных затрат на создание новых экземпляров классов. Суть его в том, что мы создаем "заготовку" объекта,
а затем можем клонировать эту заготовку для создания новых объектов с теми же характеристиками.
"""
import copy


class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state}'


class Person:
    def __init__(self, name, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at  {self.address}'


john = Person('John', Address('Akademika', 'Kharkov', 12))
jane = copy.deepcopy(
    john)  # с помощью deepcopy мы можем создавать обьект на основе существуещего,что бы потом изменить его!
jane.name = 'Jane'
jane.address.state = '13'
print(jane, john, sep='\n')
