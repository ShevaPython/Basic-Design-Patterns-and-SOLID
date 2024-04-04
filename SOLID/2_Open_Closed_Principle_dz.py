"""
Задача:
Представьте, что у вас есть система для отправки уведомлений пользователям. Сейчас вы поддерживаете только отправку
уведомлений по электронной почте. Однако в будущем вы хотите добавить поддержку отправки SMS-уведомлений без
 изменения существующего кода.

Ваша задача:

- Перепишите существующий код, чтобы он соответствовал принципу Open/Closed (O).
- Добавьте поддержку отправки SMS-уведомлений без изменения существующего кода.

"""
from abc import ABC, abstractmethod


class SystemSendMessage(ABC):
    @abstractmethod
    def send_message(self, message):
        pass


class SystemSendSMS(SystemSendMessage):
    def send_message(self, message):
        print(f"Sending SMS: {message}")


class SystemSendEmail(SystemSendMessage):
    def send_message(self, message):
        print(f"Sending Email: {message}")


# Пример использования
sms_sender = SystemSendSMS()
sms_sender.send_message("Hello, this is a test SMS")

email_sender = SystemSendEmail()
email_sender.send_message("Hello, this is a test email")
