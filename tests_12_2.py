import unittest
import runner_and_tournament as runner

'''
В runner_and_tournament,в class Runner нужно добавить:
    def __repr__(self):
        return self.name
чтобы вместо адреса можно было выводить имя бегуна.

Также допущена ошибка в class Tournament в def start(self):
                if participant.distance > self.full_distance:
При >= (изначальное значение в коде) в последнем тесте возникает ошибка правильной очередности.
'''


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = runner.Runner("Усэйн", 10)
        self.andrei = runner.Runner("Андрей", 9)
        self.nik = runner.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test1(self):
        tournament = runner.Tournament(90, self.usein, self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.nik)

    def test2(self):
        tournament = runner.Tournament(90, self.andrei, self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.nik)

    def test3(self):
        tournament = runner.Tournament(90, self.andrei, self.usein, self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.nik)


if __name__ == '__main__':
    unittest.main()
