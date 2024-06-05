# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение) в зависимости
# от переданных аргументов.

def division_by_n(n):
    if 0 < n <= 100:
        def quotient(x):
            return round(x / n, 2)
    elif n > 100:
        def quotient(x):
            return round(x / (n * 0.5), 2)

    elif n <= 0:
        raise Exception('Некорректно указан делитель')

    else:
        raise Exception('Что-то пошло не так')

    return quotient


my_numbers = [52, 75, 110, 150, 171, 383]
a = division_by_n(55)
b = division_by_n(132)

result = map(a, my_numbers)
print(list(result))

result = map(b, my_numbers)
print(f'{list(result)}\n')

# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
# Например, возведение числа в квадрат

my_func = lambda x: x ** 2
print(f'Задача 2, лямбда:\n{my_func(x=17)}')


def calc(x):
    if x > 0:
        return x ** 2


print(f'{calc(x=17)}\n')


#
# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, который возвращает площадь
# прямоугольника, то есть a*b.


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


my_rectangle = Rect(a=7, b=12)
# my_rect.__call__()
print(
    f'Задача 3: вызываемый объект.\nСтороны - {my_rectangle.a}, {my_rectangle.b}.\nПлощадь: {my_rectangle.__call__()}')
