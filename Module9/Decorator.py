# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.


def is_prime(*args):
    def dec(num1, num2, num3):
        num = int(num1 + num2 + num3)

        def wrapper():
            if num == 0:
                return "Не является ни простым, ни составным числом"
            if num == 1:
                return "Не является ни простым, ни составным числом"
            for i in range(2, num):
                if num % i == 0:
                    return "Составное"
            return "Простое"

        print(f'{wrapper()}\n{num}')

    return dec


@is_prime
def summ_three(a, b, c):
    x = a + b + c
    return x


result = summ_three(2, 3, 6)
print(result)
