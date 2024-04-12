"""
Декораторы классов - это способ динамического изменения поведения класса путем оборачивания его в другой класс.
Этот паттерн позволяет добавлять новое поведение или функциональность классу без изменения его основной реализации.

Примеры декораторов на основе классов могут быть различными. Давайте рассмотрим несколько примеров:

Логирование: Декоратор класса может добавить логирование к каждому методу класса для отслеживания его действий.

Кэширование: Декоратор класса может кэшировать результаты вызовов методов класса для повышения производительности.

Аутентификация и авторизация: Декоратор класса может проверять права доступа пользователя к методам класса.

Давайте рассмотрим пример декоратора класса для логирования:
"""

class Logger:
    def __init__(self, component):
        self.component = component

    def log(self, message):
        print(f'LOG: {message}')

    def __getattr__(self, name):
        return getattr(self.component, name)

    def __setattr__(self, name, value):
        if name == 'component':
            self.__dict__[name] = value
        else:
            self.log(f'Setting {name} to {value}')
            setattr(self.component, name, value)
    def __str__(self):
        return str(self.component)

# Пример использования:

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result
    def __str__(self):
        return f'Result: {self.result}'

# Оборачиваем класс Calculator в декоратор Logger
calculator = Logger(Calculator())

# Вызываем метод add, который будет логировать свое действие
calculator.add(2, 3)
print("Calculator: ",calculator)


