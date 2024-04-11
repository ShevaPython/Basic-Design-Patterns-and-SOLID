from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    Cartesian = 1
    Polar = 2


class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'Point(x={self.__x}, y={self.__y})'

    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            """Создаем методы которые создают обьект за нас"""
            p = Point()
            p.__x = x
            p.__y = y
            return p

        @staticmethod
        def new_polar_point(rho, theta):
            """Создаем методы которые создают обьект за нас"""
            return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point.PointFactory.new_polar_point(2, 3)
    print(p1, p2, sep="\n")
