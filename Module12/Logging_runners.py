import unittest
import logging
import rt_with_exceptions as rt


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            obj = rt.Runner('Mike', speed=-5)
            for _ in range(1, 11):
                obj.walk()
            # self.assertEqual(self.mike.distance, 50)
            logging.INFO(f"test_walk выполнен успешно")
        except ValueError:
            logging.warning("Неверная скорость для  Runner", exc_info=True)

    def test_run(self):
        try:
            obj = rt.Runner(121)
            for _ in range(1, 11):
                obj.run()
            logging.INFO('test_run выполнен успешно')

        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


# first = Runner('Вася', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="r", filename='runner_tests.py', encoding='UTF-8 ',
                        format="%(asctime)s | %(levelname)s | %(message)s")
