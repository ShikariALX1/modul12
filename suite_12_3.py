import unittest
import tests_12_3 as test

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)