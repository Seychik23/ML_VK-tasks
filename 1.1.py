from datetime import datetime

def sort_by_name(data):
    return sorted(data, key=lambda x: x[0])

def sort_by_average_check(data):
    return sorted(data, key=lambda x: float(x[1]))

def sort_by_birth_date(data):
    return sorted(data, key=lambda x: datetime.strptime(x[2], "%d.%m.%Y"))

# Чтение входных данных
N = int(input().strip())  # Число строк
data = []

for _ in range(N):
    line = input().strip()
    # Проверка на корректность формата
    if line:
        parts = line.split(", ")
        if len(parts) == 3:
            name, average_check, birth_date = parts
            data.append((name, average_check, birth_date))
        else:
            print(f"Ошибка: строка '{line}' не соответствует формату 'имя, средний чек, дата рождения'.")

# Сортировка данных
sorted_by_name = sort_by_name(data)
sorted_by_check = sort_by_average_check(data)
sorted_by_birth_date = sort_by_birth_date(data)

# Вывод результатов
for entry in sorted_by_name:
    print(", ".join(entry))
print("#")
for entry in sorted_by_check:
    print(", ".join(entry))
print("#")
for entry in sorted_by_birth_date:
    print(", ".join(entry))
