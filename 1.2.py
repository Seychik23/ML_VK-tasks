import math

def truesqrt(n):
    if n < 0:
        raise ValueError("Входное значение должно быть неотрицательным.")

    sqrtv = math.sqrt(n)
    return -sqrtv, sqrtv

# Чтение входных данных
n = float(input().strip())

try:
    # Получение значений квадратного корня
    a, b = truesqrt(n)
    # Вывод результата
    print(f'{a} {b}')
except ValueError as e:
    print(e)
