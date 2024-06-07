# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне. При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)
# Примечание
# Значение атрибута start всегда меньше значения атрибута end
# В решении задачи не использовать list, tuple и др. встроенные типы данных.
# Входные данные
# en = EvenNumbers(10, 25)
# for i in en:
# print(i)
# Выходные данные
# После перебора и вывода:
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24

class EvenNumbers:

    def __init__(self, start, end):
        self.start = start
        if self.start == None:
            self.start = 0
        self.end = end
        if self.end == None:
            self.end = 1

        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        for self.i in range(self.start, self.end):
            if self.i % 2 == 0:
                print(self.i)
            elif self.start == None:
                self.start = 0
            elif self.end == None:
                self.end = 1
                print(self.i)

        raise StopIteration


obj = EvenNumbers(10, 25)

for value in obj:
    print(value)
