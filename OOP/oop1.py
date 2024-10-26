# Отдельный класс для обработки запросов к объекту с именем 'object_1'
class Object1Handler:
    # Метод  только для объектов с именем 'object_1'
    def supports(self, obj) -> bool:
        return obj.get_object_name() == "object_1"

    # Метод обрабатывает объект и возвращает строку, описывающую действие
    def handle(self, obj) -> str:
        return "handle_object_1"


# Отдельный класс для обработки запросов к объекту с именем 'object_2'
class Object2Handler:
    # Метод  только для объектов с именем 'object_2'
    def supports(self, obj) -> bool:
        return obj.get_object_name() == "object_2"

    # Метод обрабатывает объект и возвращает строку, описывающую действие
    def handle(self, obj) -> str:
        return "handle_object_2"


# Конструктор класса
class SomeObject:
    def __init__(self, name: str):
        self.name = name

    # Метод возвращает имя объекта
    def get_object_name(self) -> str:
        return self.name


# Класс, обрабатывающий список объектов с помощью различных обработчиков
class SomeObjectsHandler:
    def __init__(self, handlers):
        # Принимает список обработчиков и сохраняет их для дальнейшего использования
        self.handlers = handlers

    def handle_objects(self, objects):
        results = []
        for obj in objects:
            # Цикл по каждому обработчику из списка обработчиков
            for handler in self.handlers:
                if handler.supports(obj):
                    # Выполнить обработку объекта с помощью текущего обработчика и добавить результат в результат
                    results.append(handler.handle(obj))
                    # Прерывание обработчик для объекта уже найден
                    break
        # На возврат идет список обработанных объектов
        return results


# Список объектов для обработки
objects = [
    SomeObject("object_1"),
    SomeObject("object_2"),
]
# Список доступных обработчиков
handlers = [
    Object1Handler(),
    Object2Handler(),
]
soh = SomeObjectsHandler(handlers)
print(soh.handle_objects(objects))
