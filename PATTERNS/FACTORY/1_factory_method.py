"""
Создает обьект целиком а не как билдер аошагово!
Фабрика (Factory) - это порождающий паттерн проектирования, который предоставляет интерфейс для создания экземпляров
различных объектов в суперклассе, а затем позволяет подклассам изменять тип создаваемых объектов.

Основная идея фабрики состоит в том, чтобы вынести процесс создания объектов из клиентского кода
в отдельные методы или классы. Это позволяет легко добавлять новые типы объектов без изменения существующего клиентского кода.
"""
from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    Cartesian = 1
    Polar = 2


class Point:
    # def __init__(self, a, b, system=CoordinateSystem.Cartesian):
    #     if system == CoordinateSystem.Cartesian:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.Polar:
    #         self.x = a * sin(b)
    #         self.y = a * cos(b)
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'Point(x={self.__x}, y={self.__y})'

    @staticmethod
    def new_cartesian_point(x, y):
        """Создаем методы которые создают обьект за нас"""
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        """Создаем методы которые создают обьект за нас"""
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point.new_polar_point(2,3)
    print(p1,p2,sep="\n")
