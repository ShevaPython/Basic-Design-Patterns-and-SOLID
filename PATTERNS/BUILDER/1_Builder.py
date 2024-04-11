""""
Builder -
Паттерн Строитель - это порождающий паттерн проектирования, который используется для создания объектов с составными
параметрами. Он позволяет создавать различные конфигурации объектов, используя один и тот же процесс строительства.

Основная идея паттерна Строитель состоит в том, чтобы разделить процесс создания сложного объекта на несколько этапов.
Затем клиентский код может использовать строитель для пошагового построения объекта, внося необходимые изменения на
каждом этапе.

"""


class House:
    """
    House: Это класс, представляющий объект дома. У него есть атрибуты, такие как количество этажей (floors),
    количество комнат (rooms), наличие сада (garden) и гаража (garage). Он также определяет метод __str__,
    который возвращает строковое представление объекта.
    """

    def __init__(self, floor=1, room=1, garden=False, garage=False):
        self.floor = floor
        self.room = room
        self.garden = garden
        self.garage = garage

    def __str__(self):
        return f'House with Floor: {self.floor}, Room: {self.room}, Garden: {self.garden}, Garage: {self.garage}'


class HouseBuilder:
    """
    HouseBuilder: Это класс строителя, который отвечает за построение объектов House. Он инициализирует пустой объект House
    в своем конструкторе. Затем он предоставляет методы для пошагового задания параметров объекта House: set_floors,
    set_rooms, add_garden и add_garage. В конце концов, он предоставляет метод build, который возвращает готовый объект
    House.
    """

    def __init__(self):
        self.house = House()

    def set_floor(self, value):
        self.house.floor = value
        return self

    def set_room(self, value):
        self.house.room = value
        return self

    def add_garden(self):
        self.house.garden = True
        return self

    def add_garage(self):
        self.house.garage = True
        return self

    def build(self):
        return self.house


builder = HouseBuilder()
house = builder.set_room(2).set_floor(2).add_garage().add_garden().build()

print(house)
