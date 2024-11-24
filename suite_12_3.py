import unittest
from tests_12_3 import RunnerTest, TournamentTest

modules_12ST = unittest.TestSuite()
modules_12ST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
modules_12ST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(modules_12ST)
