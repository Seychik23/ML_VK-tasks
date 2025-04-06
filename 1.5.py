input_a = input()
set_a = set(map(int, input_a.split()))

input_b = input()
set_b = set(map(int, input_a.split()))

def difference(set_a, set_b):
    result = set()  # Создаем пустое множество для результата
    for element in set_a:  # Итерируем по элементам первого множества
        if element not in set_b:  # Проверяем, есть ли элемент во втором множестве
            result.add(element)  # Если нет, добавляем его в результат
    return result  # Возвращаем результирующее множество
