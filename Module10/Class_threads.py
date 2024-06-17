import time
from threading import Thread
from collections import defaultdict
from time import sleep, time
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
                if enemy_remains == 0:
                    break
                enemy_remains = enemy - self.skill*counter

                print(f'{self.name} сражается {counter} день, убито {self.skill} воинов, осталось {enemy_remains} врагов')
        if enemy_remains == 0:
            print(f'{self.name} одержал победу  спустя {counter - 1} дней!')


        # time.sleep(1)
        # if time.sleep(1):
        #     print("")
        # enemy_killed = defaultdict(int)
        # for person in range(enemy):
        #     print(f'{self.name} сражается, убито {self.skill} воинов, осталось {enemy - self.skill} врагов')
        # if enemy_killed == enemy:
        #     print("Все враги уничтожены, битва закончилась")


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

print(f'{knight1.name}: святые угодники, на нас напали!')
print(f'{knight2.name}: OMG, на нас напали!')

knight1.start()
knight2.start()



knight1.join()
knight2.join()

print("Все битвы закончились")



