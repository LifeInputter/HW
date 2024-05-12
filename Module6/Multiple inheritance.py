class Vehicle:

    def __init__(self):
        self.vehicle_type = None


class Car:

    def __init__(self):
        self.price = 1000000

    def horse_power(self):
        self.horse_power = None

    def __str__(self):
        return '{} мощность {}'.format(self.__class__.__name__, self.horse_power())


class Nissan(Car, Vehicle):


    def __init__(self, name):
        self.horse_power = 250
        self.price = 1500000
        self.vehicle_type = "sport car"
        self.name = name

        # super().__init__(vehicle_type)

    def __str__(self):
        return '{} модель {}, мощность {}. Тип ТС - {}, цена - {} '.format(self.__class__.__name__, self.name,
                                                                        self.horse_power, self.vehicle_type, self.price)




car1 = Car()
print(car1)
print(car1.price) #проверка вывода класса Car

my_car = Nissan(name="GTR")
print(my_car)
