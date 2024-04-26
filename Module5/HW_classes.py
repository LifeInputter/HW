class House:
    numberOfFloors = 10

    for i in range(numberOfFloors):
        print("Текущий этаж равен ", i + 1)


# Вариант 2: выводит список этажей 1-10
class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 10
        for i in range(numberOfFloors):
            if i >= 0 and i <= 9:
                print("Текущий этаж равен: ", i + 1)
            else:
                print("Out of range ")


house = House(11)
