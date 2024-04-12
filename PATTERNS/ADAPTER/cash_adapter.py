import requests
import json

"""
В этом примере RemoteAPI - это класс, который предоставляет метод fetch_data() для получения данных с удаленного сервера.
CacheAdapter - это адаптер, который оборачивает RemoteAPI и добавляет механизм кеширования. Когда клиент вызывает fetch_data(),
CacheAdapter проверяет, есть ли данные в кеше, и возвращает их, если они есть. Если данных нет в кеше, CacheAdapter
обращается к RemoteAPI, получает данные, сохраняет их в кеш и возвращает клиенту."""


class RemoteAPI:
    def fetch_data(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None


class CacheAdapter:
    def __init__(self, remote_api):
        self.remote_api = remote_api
        self.cache = {}

    def fetch_data(self, url):
        if url in self.cache:
            print("Retrieving data from cache...")
            return self.cache[url]
        else:
            print("Fetching data from remote API...")
            data = self.remote_api.fetch_data(url)
            self.cache[url] = data
            return data


# Использование
remote_api = RemoteAPI()
adapter = CacheAdapter(remote_api)

data1 = adapter.fetch_data("https://api.example.com/data")  # Первый запрос, данные получены из API
data2 = adapter.fetch_data("https://api.example.com/data")  # Второй запрос, данные получены из кеша

print(data1)
print(data2)
