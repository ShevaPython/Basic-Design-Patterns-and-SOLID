"""
DIP -
Принцип инверсии зависимостей (Dependency Inversion Principle, DIP) является одним из принципов SOLID.
Он предлагает способ организации кода таким образом, чтобы зависимости между классами были слабыми и управляемыми.

Основная идея принципа заключается в том, что модули верхнего уровня не должны зависеть от модулей нижнего уровня.
Оба уровня должны зависеть от абстракций, а не от конкретных реализаций. Также он гласит о том, что абстракции
не должны зависеть от деталей реализации, а детали реализации должны зависеть от абстракций.

Это достигается путем введения абстракций и обращения к ним вместо прямого использования конкретных классов или
модулей. Это позволяет легко изменять или заменять реализацию компонентов системы, не затрагивая другие части кода.

Принцип DIP способствует созданию более гибких, расширяемых и легко тестируемых приложений. Он также способствует
уменьшению связности и повышению переиспользуемости кода.
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)