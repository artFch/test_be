# Класс определяет метод request, он главный класс и подклассы должны реализовывать метод
class HttpService:
    def request(self, url: str, method: str, options=None):
        pass  # Метод должен быть реализован в подклассах


# Класс наследующий класс HttpService, он реализует метод request и выводит что делает запрос
class XMLHttpService(HttpService):
    def request(self, url: str, method: str, options=None):
        print(f"Requesting {method} {url} with options: {options}")


# Класс Http, который использует любой подкласс класса HttpService, и использует его для выполнения запросов
class Http:
    def __init__(self, service: HttpService):
        self.service = service

    def get(
        self, url: str, options=None
    ):  # В примере у GET есть options а у POST нет, поэтому сделаю его опциональным
        self.service.request(url, "GET", options)

    def post(self, url: str, options=None):
        self.service.request(url, "POST", options)
