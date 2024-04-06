"""
Задание:
1.Создайте базовый класс Person с атрибутами name и age, и методом get_info(), который возвращает информацию о человеке в виде строки.
2.Создайте подклассы Student и Teacher, которые наследуются от Person.
3.Для класса Student переопределите метод get_info(), чтобы он возвращал информацию о
 студенте в формате "Имя: [name], Возраст: [age], Статус: Студент".
4.Для класса Teacher также переопределите метод get_info(), чтобы он возвращал информацию о преподавателе
 в формате "Имя: [name], Возраст: [age], Статус: Преподаватель".

Проверка:
Создайте экземпляры объектов классов Student и Teacher с разными именами и возрастами, а затем вызовите
 метод get_info() для каждого из них. Убедитесь, что возвращаемые значения соответствуют ожидаемой информации для каждого типа человека.

"""
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Student(Person):
    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Статус: Студент"


class Teacher(Person):
    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Статус: Преподаватель"


def _get_info(person):
    print(person.get_info())


student = Student("Maik", 20)
teacher = Teacher("Ronny", 49)

_get_info(student)
_get_info(teacher)
