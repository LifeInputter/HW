import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.mike = Runner('Mike')
        for _ in range(1, 11):
            self.mike.walk()
        self.assertEqual(self.mike.distance, 50)

    def test_run(self):
        self.garry = Runner("Garry")
        for _ in range(1, 11):
            self.garry.run()
        self.assertEqual(self.garry.distance, 100)

    def test_challenge(self):
        self.garry = Runner("Garry")
        self.mike = Runner('Mike')
        for _ in range(1, 11):
            self.garry.run()
            self.mike.walk()
        self.assertNotEqual(self.garry.distance, self.mike.distance)
