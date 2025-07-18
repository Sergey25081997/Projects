# Домашнее задание 18
# Написать генераторы чисел фибоначчи и простых чисел. Функция генератор на вход должна аргументом принять ограничение (генерация всех простых чисел до 100_000, например)

def fibonacci(limit):
    """
    Генератор чисел Фибоначчи до limit (не включая limit).

    Аргументы:
        limit (int): Верхняя граница последовательности
                     (числа Фибоначчи будут меньше этого значения).

    Возвращает:
        int: Следующее число Фибоначчи (при каждой итерации цикла).

    Пример использования:
        for num in fibonacci(100000):
            print(num)
    """
    a, b = 0, 1  # Начальные два числа Фибоначчи
    while a < limit:
        yield a       # Возвращаем текущее число Фибоначчи
        a, b = b, a + b  # Пересчитываем два следующих числа

for num in fibonacci(100_000):
    print(num)

def primes(limit):
    """
    Генератор простых чисел до limit (не включая limit).

    Аргументы:
        limit (int): Верхняя граница для поиска простых чисел
                     (простые числа будут меньше этого значения).

    Возвращает:
        int: Следующее простое число (при каждой итерации цикла).

    Пример использования:
        for prime in primes(100000):
            print(prime)
    """
    for num in range(2, limit):  # Перебираем числа от 2 до limit-1
        # Проверяем, делится ли num нацело на какое-либо из меньших чисел
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                break  # Если делится — не простое, переходим к следующему числу
        else:
            yield num  # Если не делится — это простое число, возвращаем его

for prime in primes(100_000):
    print(prime)

"""
Как работают генераторы
Генератор Фибоначчи сохраняет только два последних значения и всегда знает, какое выдать следующее.
Генератор простых чисел для каждого числа проверяет, делится ли оно на любое число меньше его квадратного корня (так быстрее, чем проверять делимость на все числа подряд).
Оба генератора эффективны по памяти: они "генерируют" числа по требованию, а не держат весь список сразу.
"""