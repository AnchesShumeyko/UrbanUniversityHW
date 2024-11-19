import unittest
import runner # импортирован модуль с классом Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_ = runner.Runner('Penguin')
        for _ in range(10):
            runner_.walk()
        self.assertEqual(runner_.distance, 45) # изменено значение равенства, данный тест не пройден

    def test_run(self):
        runner_ = runner.Runner('Koala')
        for _ in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_challenge(self):
        runner1 = runner.Runner('Turtle')
        runner2 = runner.Runner('Snail')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':

    unittest.main()





