# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.


def is_prime(func):
    def wrapper():
        n= func
        # original_res = n
        # wrapped_res =
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False

        return True #("Простое")
    return wrapper()

print(is_prime(1))
#
#
@is_prime          # если отключить декоратор, то по-отдельности все работвет.
def summ_three(a, b, c):
    summ = a+b+c
    return summ

result = summ_three(2,3,6)
print(int(summ_three(2,3,6)))