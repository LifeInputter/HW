from random import randint

from termcolor import colored, cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'я - {}, сытость {}'.format(
            self.name, self.fullness, self.house.food, self.house.money)

    def eat(self):
        if self.house.food >= 10:
            cprint("{} поел".format(self.name), color='cyan')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет  еды'.format(self.name), color='red')

    def work(self):
        cprint('{} ходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились'.format(self.name), color='red')

    def go_into_house(self, house):
        self.house = house
        cprint('{} Заехал в дом!'.format(self.name), color='cyan')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('{}умер'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:
    def __init__(self):
        self.food = 50
        self.money = 10

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(
            self.food, self.money)


citizens = [
    Man(name="Бивис"),
    Man(name="Батхед"),
    Man(name='Кенни')
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_house(house=my_sweet_home)

# print(vasya)
# vasya.eat()
# print(vasya)
# vasya.work()
# print(vasya)
# vasya.play_DOTA()
# print(vasya)
for day in range(1, 366):
    cprint('=============== день {} ================'.format(day), color='yellow')
    for citizen in citizens:
        citizen.act()
    print('-----------------в конце дня--------------')
    for citizen in citizens:
        print(citizen)
    # print(beavis)
    # print(butthead)
    print(my_sweet_home)
