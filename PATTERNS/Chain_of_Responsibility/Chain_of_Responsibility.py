"""
 Паттерн "Цепочка обязанностей" (Chain of Responsibility) представляет собой поведенческий паттерн проектирования,
который позволяет передавать запросы последовательно по цепочке обработчиков. Запрос просматривается каждым обработчиком
в цепочке до тех пор, пока не будет найден тот, который может его обработать.

Рассмотрим следующую ситуацию: у вас есть несколько объектов, каждый из которых способен обработать некоторый
запрос, но вы не знаете заранее, какой объект должен это делать. В этом случае можно создать цепочку из обработчиков,
где каждый объект решает, может ли он обработать запрос, и если нет, передает его следующему обработчику в цепочке.

Пример: допустим, у нас есть система обработки запросов на сервере, где каждый обработчик может обрабатывать
запрос определенного типа. Если первый обработчик не может обработать запрос, он передает его следующему,
и так далее, пока запрос не будет успешно обработан или пока не будут исчерпаны все обработчики.
"""


class AuthHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            return self.successor.handle_request(request)
        return None


class TokenAuthHandler(AuthHandler):
    def handle_request(self, request):
        if request.get('token'):
            return f"Token authentication successful for user '{request['user']}'"
        else:
            return super().handle_request(request)


class SessionAuthHandler(AuthHandler):
    def handle_request(self, request):
        if request.get('session_id'):
            return f"Session authentication successful for user '{request['user']}'"
        else:
            return super().handle_request(request)


class ApiKeyAuthHandler(AuthHandler):
    def handle_request(self, request):
        if request.get('api_key'):
            return f"API key authentication successful for user '{request['user']}'"
        else:
            return super().handle_request(request)


# Клиентский код
def authenticate_request(handler, request):
    result = handler.handle_request(request)
    if result:
        print(result)
    else:
        print("Authentication failed")


# Создание цепочки обработчиков
token_handler = TokenAuthHandler()
session_handler = SessionAuthHandler()
api_key_handler = ApiKeyAuthHandler()

# Установка последовательности обработчиков
token_handler.successor = session_handler
session_handler.successor = api_key_handler

# Подготовка запросов на авторизацию
requests = [
    {'user': 'Alice', 'token': 'abc123'},
    {'user': 'Bob', 'session_id': 'session123'},
    {'user': 'Charlie', 'api_key': 'xyz456'},
    {'user': 'Dave', 'password': 'qwerty'}  # Неопределенный запрос
]

# Аутентификация запросов
for request in requests:
    authenticate_request(token_handler, request)
