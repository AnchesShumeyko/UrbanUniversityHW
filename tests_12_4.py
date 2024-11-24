import logging
import unittest
import module_12_4  # содержит обновленную версию классов Runner и Tournament из ссылки на GitHub в задаче


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_ = module_12_4.Runner('Penguin', -2)
            for _ in range(10):
                runner_.walk()
                self.assertEqual(runner_.distance, 50)
                logging.info('test_walk" выполнен успешно')

        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner2 = module_12_4.Runner(2)
            for _ in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner1 = module_12_4.Runner('Turtle')
        runner2 = module_12_4.Runner('Snail')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


logging.basicConfig(filename="runner_test.log", level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(message)s")
