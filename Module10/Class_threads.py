# Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.
# Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени потребуется рыцарю, чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.
import time
from threading import Thread
from termcolor import cprint
from collections import defaultdict
from time import sleep


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        enemy = 100
        enemy_remains = 100
        counter = 0
        if enemy >= 0:
            for i in range(20):
                counter += 1
                time.sleep(1)
                if enemy_remains == 0:
                    break
                enemy_remains = enemy - self.skill * counter

                print(
                    f'{self.name} сражается {counter} день, убито {self.skill} воинов, осталось {enemy_remains} врагов',
                    flush=True)
        if enemy_remains == 0:
            cprint(f'{self.name} одержал победу  спустя {counter - 1} дней!', color='cyan')


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

cprint(f'{knight1.name}: святые угодники, на нас напали!', color="yellow")
cprint(f'{knight2.name}: OMG, на нас напали!', color="yellow")

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("-"*10,"Все битвы закончились","-"*10)
