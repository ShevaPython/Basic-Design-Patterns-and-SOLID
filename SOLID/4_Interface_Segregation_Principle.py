"""
ISP -- принцип разделения интерфейса!
Этот принцип утверждает, что интерфейсы должны быть специфичными для клиентов, которые их используют,
и не должны содержать лишних методов, которые не используются клиентами. Другими словами,
большие интерфейсы следует разбивать на более мелкие и специфичные, чтобы избежать "жирных" интерфейсов,
которые заставляют клиентов реализовывать методы, которые им не нужны.

Принцип разделения интерфейса имеет следующие ключевые идеи:

1. интерфейсов: Интерфейсы должны быть специфичными для клиентов, которые их используют.
Это означает, что интерфейс должен предоставлять только те методы, которые реально нужны клиенту для выполнения его задачи.

2.Разделение обязанностей: Разделение интерфейсов помогает разделить обязанности между классами и уменьшить
связанность между ними. Это делает код более гибким и упрощает его поддержку и изменение.

3.Избегание "жирных" интерфейсов: "Жирные" интерфейсы содержат много методов, которые могут быть
не нужны клиентам. Использование таких интерфейсов может привести к ненужным зависимостям
и сложностям при поддержке кода.

"""
from abc import ABC, abstractmethod


# class Machine(ABC):
#     """
#     Жирный интерфейс который можно разбить на мелкие
#     """
#     @abstractmethod
#     def print(self, document):
#         raise NotImplementedError
#
#     def fax(self, document):
#         raise NotImplementedError
#
#     def scan(self, document):
#         raise NotImplementedError


# class MultiFunctionPrinter(Machine):
#     """
#     Жирный интерфейс который можно разбить на мелкие
#     """
#
#     def print(self, document):
#         pass
#
#     def fax(self, document):
#         pass
#
#     def scan(self, document):
#         pass


class OldFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass  # noop

    def scan(self, document):
        """Not supported"""
        raise NotImplementedError("Printer can not scan!")


class Printer(ABC):
    """Мелкие интерфейсы"""

    @abstractmethod
    def print(self, document):
        raise NotImplementedError


class Scaner(ABC):
    """Мелкие интерфейсы"""

    @abstractmethod
    def scan(self, document):
        raise NotImplementedError


class Fax(ABC):
    """Мелкие интерфейсы"""

    @abstractmethod
    def fax(self, document):
        raise NotImplementedError


class Myprinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scaner):
    def print(self, document):
        print("Print... document", document)

    def scan(self, document):
        print("Scanned! document:", document)


class MultiFunctionPrinter(Printer, Scaner, Fax):
    """Правильный интерфейс для пользователя"""
    def print(self, document):
        print("Print... document", document)

    def scan(self, document):
        print("Scanned! document:", document)

    def fax(self, document):
        print("Faxed! document:", document)
