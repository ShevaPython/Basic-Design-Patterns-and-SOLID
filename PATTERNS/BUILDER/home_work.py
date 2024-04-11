"""
Представьте, что у вас есть класс Meal, который представляет собой блюдо в ресторане.
У блюда может быть несколько компонентов, таких как гарнир, напиток и основное блюдо. Вам нужно реализовать строитель MealBuilder, который позволит создавать экземпляры класса Meal с различными компонентами.

Ваша задача:

1.Определить класс Meal с атрибутами main_course (основное блюдо), side_dish (гарнир) и drink (напиток).
2.Создать класс MealBuilder, который позволяет настраивать компоненты блюда.
3.Реализовать методы в MealBuilder для установки основного блюда, гарнира и напитка.
4.Добавить метод build, который создает и возвращает экземпляр класса Meal с настроенными компонентами.
"""


class Meal:
    def __init__(self):
        self.main_course = None
        self.side_dish = None
        self.drink = None

    def __str__(self):
        return f'Main_course: {self.main_course}, Side_dish: {self.side_dish},Drink: {self.drink}'

    @staticmethod
    def new():
        return MealBuilder()


class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def build(self):
        return self.meal


class MealMainCourse(MealBuilder):
    def set_main_course(self, main_course):
        self.meal.main_course = main_course
        return self


class MealSideDish(MealMainCourse):
    def set_side_dish(self, side_dish):
        self.meal.side_dish = side_dish
        return self


class MealDrink(MealSideDish):
    def set_drink(self, drink):
        self.meal.drink = drink
        return self


builder = MealDrink()
meal = builder \
    .set_main_course('Steak') \
    .set_side_dish('Mashed potatoes') \
    .set_drink('Red wine') \
    .build()

print(meal)
# Создаем новый строитель
builder2 = MealDrink()

# Настройка компонентов заказа
meal2 = builder2 \
    .set_main_course('Salmon') \
    .set_side_dish('Steamed vegetables') \
    .build()

# Вывод информации о втором заказе
print(meal2)
