# Задание
# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки. В функцию передаётся только сама строка.
# Примечание
# Используйте оператор yield
# Входные данные
# a = all_variants("abc")
# for i in a:
# print(i)

def all_variants(text):
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


a = all_variants("abc")
for i in a:
    print(i)
