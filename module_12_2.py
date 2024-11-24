import tournament
import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = tournament.Runner('Усейн', 10)
        self.runner2 = tournament.Runner('Андрей', 9)
        self.runner3 = tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):  # "????"
        for tournament_name, placements in cls.all_results.items():
            result_str = f'{tournament_name} тур. ' + ', '.join(
                f'{place}: {runner.name}' for place, runner in placements.items())
            print(result_str)

    def test_tournament_1(self):
        tour1 = tournament.Tournament(90, self.runner1, self.runner3)
        results = tour1.start()
        TournamentTest.all_results[1] = results
        self.assertEqual(list(results.values())[-1].name, 'Ник')
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_tournament_2(self):
        tour2 = tournament.Tournament(90, self.runner2, self.runner3)
        results = tour2.start()
        TournamentTest.all_results[2] = results
        self.assertEqual(list(results.values())[-1].name, 'Ник')
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_tournament_3(self):
        tour3 = tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tour3.start()
        TournamentTest.all_results[3] = results
        self.assertEqual(list(results.values())[-1].name, 'Ник')
        self.assertTrue(results[max(results.keys())] == self.runner3)


if __name__ == "__main__":
    unittest.main()
