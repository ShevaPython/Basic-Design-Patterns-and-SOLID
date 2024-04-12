"""
Composite - Компоновщик
Паттерн Composite применяется для создания древовидной структуры объектов, где как отдельные объекты, так и их композиции
(составные объекты) могут быть обработаны одинаково. Он позволяет клиентам обрабатывать отдельные объекты
и их композиции единообразно, что делает его полезным для работы с иерархиями объектов.
"""
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        return "Leaf operation"


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite operation: {' | '.join(results)}"


leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
print(composite.operation())
