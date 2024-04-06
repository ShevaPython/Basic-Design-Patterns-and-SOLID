"""
Требования:

Обычные пользовательские аккаунты должны иметь возможность регистрации, входа в систему и просмотра информации о своем аккаунте.

Аккаунты администраторов должны иметь возможность входа в систему, просмотра списка пользователей и выполнения дополнительных административных действий, таких как блокировка или удаление аккаунтов пользователей.

Задача:

Создайте интерфейс UserAccount, содержащий методы register(), login() и view_account_info().
Создайте интерфейс AdminAccount, содержащий методы login(), view_user_list(), block_user() и delete_user().
Реализуйте классы NormalUserAccount и AdminUserAccount, которые реализуют соответствующие интерфейсы.
Проверьте корректность работы системы, создав объекты пользовательских и администраторских аккаунтов, а затем попробуйте выполнить соответствующие действия.
Эта задача поможет вам применить Принцип разделения интерфейса (ISP) для создания более гибкой и модульной системы управления аккаунтами пользователей.
"""
from abc import ABC, abstractmethod


class UserAccount(ABC):

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    """
    Пользовательский аккаунт
    """

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def view_account_info(self):
        pass


class AdminAccount(ABC):
    """
    Администраторский аккаунт
    """

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def view_user_list(self):
        pass

    @abstractmethod
    def block_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass


class NormalUser(UserAccount):
    """
    Нормальный пользователь
    """

    def __init__(self, username=None, password=None, email=None):
        super().__init__(username, password, email)

    def register(self):
        print('Регистрация аккаунта')

    def login(self):
        print('Вход в систему')

    def view_account_info(self):
        print(F'Информация о аккаунте : \n username:{self.username} \n password:{self.password} \n email:{self.email}')


class AdminUserAccount(AdminAccount):
    """
    Администратор
    """

    def __init__(self, username=None, password=None, email=None):
        super().__init__(username, password, email)
        self.users = []  # Добавляем атрибут для хранения списка пользователей

    def login(self):
        print('Вход в систему ADMINISTRATOR')

    def view_user_list(self):
        print('Список пользователей:')
        for user in self.users:
            print(f'Username: {user.username}, Email: {user.email}')

    def view_user_info(self, username):
        for user in self.users:
            if user.username == username:
                print(f'Информация о пользователе {username}:')
                print(f'Username: {user.username}, Email: {user.email}')
                return
        print(f'Пользователь {username} не найден.')

    def block_user(self):
        print('Блокировка аккаунта username')

    def delete_user(self):
        print('Удаление аккаунта username')

    def block_user(self):
        print('Блокировка аккаунта username')

    def delete_user(self):
        print('Удаление аккаунта username')


user = NormalUser('Sergey', 123, 'sheva@gmail.com')
user.register()
user.login()
user.view_account_info()
admin = AdminUserAccount('admin', 'admin123', 'admin@example.com')
admin.users.append(NormalUser('John', 'pass123', 'john@example.com'))
admin.users.append(NormalUser('Alice', 'pass456', 'alice@example.com'))
admin.login()  # Вход в систему как администратор
admin.view_user_list()  # Просмотр списка пользователей
admin.view_user_info('John')  # Просмотр информации о пользователе John
