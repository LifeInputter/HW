import unittest
import Unittests_methods
import SimpleUnitTests

#часть 1

runner_test = unittest.TestSuite()
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(SimpleUnitTests.RunnerTest))
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Unittests_methods.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_test)

'''''
Часть 2. Пропуск тестов.
Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
'''''
from Unittests_methods import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):  # метод, где создаются 3 объекта бегуноа
        self.hussein = Runner("Уссейн", 10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner('Ник', 3)

    @classmethod  # метод, где выводятся all_results по очереди в столбец
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        attempt = Tournament(90, self.hussein, self.nick)
        result = attempt.start()
        self.all_results.append(result)
        self.assertTrue(list(result.values())[-1] == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        attempt = Tournament(90, self.andrey, self.nick)
        result = attempt.start()
        self.all_results.append(result)
        self.assertTrue(list(result.values())[-1] == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        attempt = Tournament(90, self.hussein, self.andrey, self.nick)
        result = attempt.start()
        self.all_results.append(result)
        self.assertTrue(list(result.values())[-1] == 'Ник')


if __name__ == '__main__':
    unittest.main()
