import unittest
import runner  # импортирован модуль с классом Runner
import tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner_ = runner.Runner('Penguin')
        for _ in range(10):
            runner_.walk()
        self.assertEqual(runner_.distance, 50)  # изменено значение равенства, данный тест не пройден

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner_ = runner.Runner('Koala')
        for _ in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = runner.Runner('Turtle')
        runner2 = runner.Runner('Snail')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = tournament.Runner('Усейн', 10)
        self.runner2 = tournament.Runner('Андрей', 9)
        self.runner3 = tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):  # "????"
        for place, jogger in sorted(cls.all_results.items()):
            print(f'{place} : {jogger.name}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        tour1 = tournament.Tournament(90, self.runner1, self.runner3)
        results = tour1.start()
        TournamentTest.all_results.update(results)
        self.assertEqual(list(results.values())[-1].name, 'Ник')
        self.assertTrue(results[max(results.keys())] == self.runner3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        tour2 = tournament.Tournament(90, self.runner2, self.runner3)
        results = tour2.start()
        TournamentTest.all_results.update(results)
        self.assertEqual(list(results.values())[-1].name, 'Ник')
        self.assertTrue(results[max(results.keys())] == self.runner3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        tour3 = tournament.Tournament(90, self.runner3, self.runner2, self.runner1)
        results = tour3.start()
        TournamentTest.all_results.update(results)
        self.assertEqual(list(results.values())[-1].name, 'Ник')
        self.assertTrue(results[max(results.keys())] == self.runner3)


if __name__ == '__main__':
    unittest.main()
