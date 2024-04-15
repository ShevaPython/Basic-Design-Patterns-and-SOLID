"""
Facade
Шаблон проектирования Facade (Фасад) представляет собой структурный паттерн, который предоставляет простой интерфейс к
сложной системе классов, библиотеке или фреймворку. Фасад позволяет скрыть сложность внутренней реализации системы
и предоставляет только те методы или функции, которые необходимы клиенту для работы с системой.

Основная идея фасада заключается в том, чтобы создать высокоуровневый интерфейс, который делает систему более удобной
для использования и понимания, скрывая детали реализации. Это позволяет клиентам взаимодействовать с системой без
необходимости знать о её внутреннем устройстве.
"""


class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[self.offset + index]

    def append(self, text):
        self.buffer += text


class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    # high-level
    def write(self, text):
        self.current_viewport.buffer.write(text)

    # low-level
    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
    c = Console()
    c.write('hello')
    ch = c.get_char_at(0)
