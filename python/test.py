# Python 3.11.10
from datetime import datetime


# Вспомогательная функция для вывода массива
def print_arr(arr):
    for row in arr:
        print(row)


# Функция вывода только уникальных записей по 'id', Оставляет только первую попавшеюся запись с каждым уникальным 'id'
def get_unique_rows(arr):
    seen_ids = set()

    def unique_filter(item):
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            return True
        return False

    return list(filter(unique_filter, arr))


# Функция сортировки по ключу, сортирует datetime и значения
def sort_by_key(arr, key):
    def sort_key(item):
        value = item[key]
        # Попробуем преобразовать значение в datetime
        try:
            return datetime.strptime(value, "%d.%m.%Y")
        except (ValueError, TypeError):
            return None, value  # Возвращаем None и само значение для обычной сортировки

    # Сортируем с использованием функции sort_key, функция сортирует по datetime если значение можно переоброзовать, если нет сортирует стандартно
    return sorted(
        arr, key=lambda x: (sort_key(x) if sort_key(x) is not None else (None, x[key]))
    )


# Функция фильтрации по условию, возвращает список словарей, если совпадения не найдены, возвращает сообщение "Error! Item not found"
def find_item(arr, key, value):
    result = list(filter(lambda item: item.get(key) == value, arr))
    return result if result else "Error! Item not found"


# Функция изменения структуры массива
def create_pair_map(arr):
    return dict(
        map(lambda item: (item["title"], item["id"]), arr)
    )  # Функция возвращает словарь на основе кортежей от функции map


# Выполение работы функций на тестовом массиве
array = [
    {"id": 1, "create": "14.04.2023", "title": "array1"},
    {"id": 4, "create": "09.02.2023", "title": "array4"},
    {"id": 2, "create": "03.07.2023", "title": "array2"},
    {"id": 1, "create": "22.04.2023", "title": "array1"},
    {"id": 2, "create": "12.12.2023", "title": "array4"},
    {"id": 3, "create": "04.04.2023", "title": "array3"},
]
# Задание на уникальность записей
unique_array = get_unique_rows(array)
print("Arr with unique id's:")
print_arr(unique_array)

# Задание на сортировку массива, пример выполнения с ключами 'create' и 'title'
arr_sorted_by_date = sort_by_key(unique_array, "create")
print("\nSorted by date:")
print_arr(arr_sorted_by_date)

arr_sorted_by_title = sort_by_key(unique_array, "title")
print("\nSorted by title:")
print_arr(arr_sorted_by_title)
# Задание фильтрации по условию, пример выполнения с id == 4 и title == 'array5'
print("\nItem with condition")
test_cond = find_item(unique_array, "id", 4)
print(test_cond)

print("\nItem with title = 'array5':")
test_cond_error = find_item(unique_array, "title", "array5")
print(test_cond_error)

# Задание на изменение структуры массива
array_restructured = create_pair_map(unique_array)
print("\nRestructured array:")
print(array_restructured)
