"""
Паттерн "Команда" (Command) используется для инкапсуляции запроса как объекта, позволяя тем самым параметризовать
клиентов с запросами, ставить запросы в очередь, логировать их, а также поддерживать отмену операций. Давайте рассмотрим примеры использования паттерна "Команда".

Управление действиями в пользовательском интерфейсе: Паттерн "Команда" широко используется в GUI-фреймворках
для управления действиями, такими как нажатия кнопок, выбор элементов в меню и другие пользовательские взаимодействия. Каждая команда может быть представлена отдельным классом, который инкапсулирует логику выполнения определенного действия.

Транзакции в базах данных: В базах данных команда может представлять транзакцию. Например, команда INSERT в
базу данных может быть представлена отдельным объектом класса, содержащим информацию о вставляемых данных.
Таким образом, мы можем добавить команду INSERT в очередь команд и выполнить их в определенном порядке,
обеспечивая тем самым целостность данных.

Отмена и повторение операций: Паттерн "Команда" позволяет реализовать механизм отмены и повторения операций.
Каждая команда может иметь методы undo() и redo(), которые позволяют отменять и повторять выполненные операции.


"""
from abc import ABC, abstractmethod

# Абстрактный класс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Конкретная команда для добавления элемента в список
class AddCommand(Command):
    def __init__(self, item, list):
        self.item = item
        self.list = list

    def execute(self):
        self.list.append(self.item)

    def undo(self):
        self.list.remove(self.item)

# Конкретная команда для удаления элемента из списка
class RemoveCommand(Command):
    def __init__(self, item, list):
        self.item = item
        self.list = list

    def execute(self):
        self.list.remove(self.item)

    def undo(self):
        self.list.append(self.item)

# Класс, представляющий историю команд
class CommandHistory:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)

    def undo_last_command(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()

# Использование команд
if __name__ == "__main__":
    shopping_list = []

    history = CommandHistory()

    add_bread = AddCommand("Bread", shopping_list)
    add_milk = AddCommand("Milk", shopping_list)
    remove_bread = RemoveCommand("Bread", shopping_list)

    history.execute_command(add_bread)
    print(shopping_list)  # ['Bread']

    history.execute_command(add_milk)
    print(shopping_list)  # ['Bread', 'Milk']

    history.execute_command(remove_bread)
    print(shopping_list)  # ['Milk']

    history.undo_last_command()
    print(shopping_list)  # ['Bread', 'Milk']
