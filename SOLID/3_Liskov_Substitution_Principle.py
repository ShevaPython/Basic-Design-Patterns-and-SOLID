"""
lsp --- принцип подстановки лисков,если у нас есть айпиай который принимает базовый класс,
        то мы можем передать туда любой класс и это все должно работать!

        Этот код демонстрирует классический пример нарушения Принципа подстановки Барбары Лисков (LSP), одного из
        принципов SOLID.

Принцип подстановки Барбары Лисков утверждает, что объекты суперкласса должны быть заменяемы объектами его подклассов без
влияния на корректность программы. Другими словами, подклассы должны расширять поведение, а не изменять его.

В этом коде класс Square наследуется от класса Rectangle, что интуитивно кажется логичным, поскольку квадрат "является"
прямоугольником. Однако переопределение сеттеров width и height в классе Square не ведет себя так же, как в классе
Rectangle,что нарушает принцип.

Конкретно, в классе Rectangle изменение width или height приводит к корректировке обеих размерностей, при этом сохраняя
площадь. Но в классе Square установка width или height напрямую изменяет только одну размерность, что нарушает ожидаемое
поведение квадрата.

Чтобы исправить это, необходимо не переопределять сеттеры в классе Square. Вместо этого следует сохранить поведение
согласно классу Rectangle, обеспечивая тем самым, что объект класса Square будет вести себя так же, как и объект класса
 Rectangle:
"""

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)