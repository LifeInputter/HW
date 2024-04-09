def test_params(*args, txt="Employees", **values):
    print('Сотрудники: ', values)
    for key, value in values.items():
        print(key, value)
    print(args)
    print(txt, ':', len(args))


test_params(1, 2, 3, 4, Marina='- офис-менеджер', Irina='- менеджер по продажам', Anton='- начальник отдела',
            Gleb='- управляющий')


def factorial(n):  # функция рекурсии с факториалом
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(5))
