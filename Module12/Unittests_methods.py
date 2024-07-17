
'''''
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из result и предполагаемое имя последнего бегуна (индекс -1).
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.
'''''

import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


    class TournamentTest(unittest.TestCase):

        # метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
        @classmethod
        def setUpClass(cls):
            all_results ={}

        def setUp(self):                                    # метод, где создаются 3 объекта бегуноа
            self.hussein = Runner("Уссейн", speed=10)
            self.andrey = Runner("Андрей",   speed=9)
            self.nick = Runner('Ник', speed=3)



        @classmethod                # метод, где выводятся all_results по очереди в столбец
        def tearDownClass(cls):
            print()

        def run(self, result = None):
            runners = [self.hussein, self.andrey, self.nick]
            for runner in runners:
                runner.run()
                attempt.start()
                print(result)



attempt = Tournament(distance=90)

