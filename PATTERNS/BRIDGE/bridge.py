"""
Bridge - соединение компоненнтов с помощью абстракции!
"Мост" (Bridge) - это способ разделить абстракцию от ее реализации таким образом, чтобы они могли изменяться независимо друг от друга.

Давайте представим, что у нас есть ситуация, когда у нас есть классы, имеющие несколько различных основных аспектов
(например, два вида баз данных, два вида операционных систем или два вида устройств). Мы хотим иметь возможность
комбинировать эти аспекты между собой, не привязываясь к конкретным реализациям. И здесь на помощь приходит паттерн "Мост".

В паттерне "Мост" мы имеем две отдельные иерархии классов: одна для абстракции (классы, представляющие высокоуровневую
логику) и одна для реализации (классы, представляющие конкретные реализации этой логики). Между этими двумя иерархиями
устанавливается мост, который позволяет абстракции использовать различные реализации без изменения своей структуры.


Таким образом, паттерн "Мост" позволяет нам разделять абстракцию и реализацию, что делает наш код более гибким
и расширяемым, поскольку мы можем легко добавлять новые абстракции и новые реализации, не затрагивая уже существующий код.
"""
from abc import ABC, abstractmethod


class Render(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

    @abstractmethod
    def render_square(self, side):
        pass


class RenderVector(Render):
    def render_circle(self, radius):
        print(F"Drawing a circle of radius {radius}")

    def render_square(self, side):
        print(F"Drawing a square of side {side}")


class RasterRender(Render):
    def render_circle(self, radius):
        print(F"Drawing  pixel a circle of radius {radius}")

    def render_square(self, side):
        print(F"Drawing pixel  a square of side {side}")


class Shape:
    def __init__(self, renderer):
        self.render = renderer

    def draw(self): pass

    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer: Render, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.render.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRender()
    vector = RenderVector()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
