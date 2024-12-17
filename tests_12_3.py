import runner
import unittest
import runner_and_tournament as runners


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        runner1 = runner.Runner(self)
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        runner2 = runner.Runner(self)
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        runner3 = runner.Runner(self)
        runner4 = runner.Runner(self)
        for i in range(10):
            runner3.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = runners.Runner("Усэйн", 10)
        self.andrei = runners.Runner("Андрей", 9)
        self.nik = runners.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        tournament = runners.Tournament(90, self.usein, self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        tournament = runners.Tournament(90, self.andrei, self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        tournament = runners.Tournament(90, self.andrei, self.usein, self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.nik)


if __name__ == '__main__':
    unittest.main()
