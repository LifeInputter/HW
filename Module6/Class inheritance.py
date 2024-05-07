class Car:
    price = 1000000

    def __init__(self, name=None):
        self.name = name

        # self.price = 1000000

    def horse_power(self):
        self.horse_power = "количество лошадиных сил -"
        print(self.horse_power, input("укажи мощность двигателя"))


my_car = Car()
print(f"my_car:", "цена-", my_car.price)
print(my_car.horse_power())


class Nissan(Car):
    price = 1500000

    def __init__(self):
        self.horse_power = 255

    def horse_power(self):
        pass


my_car_1 = Nissan()

print(f'my_car_1 - Ниссан.' "Цена-", my_car_1.price, "мощность двигателя -", my_car_1.horse_power)


class Kia(Car):
    price = 850000

    # def __init__(self):
    #     self.horse_power = 125

    def horse_power(self):
        self.horse_power = 127


my_car_2 = Kia
print(my_car_2.horse_power(Kia))
print(f'my_car_2 - Киа.' "Цена-", my_car_2.price, "мощность двигателя -", my_car_2.horse_power)