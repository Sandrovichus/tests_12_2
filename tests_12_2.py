import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            temp_dict = {}
            for j in cls.all_results[i]:
                temp_dict[j] = str(cls.all_results[i][j])
            print(temp_dict)

    def test_run_1(self):
        tournament1 = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = tournament1.start()
        self.assertTrue(self.all_results[1][max(self.all_results[1].keys())] == 'Ник')

    def test_run_2(self):
        tournament2 = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = tournament2.start()
        self.assertTrue(self.all_results[2][max(self.all_results[2].keys())] == 'Ник')

    def test_run_3(self):
        tournament3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = tournament3.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3].keys())] == 'Ник')

    def test_run_4(self):
        tournament3 = Tournament(1, self.runner_3, self.runner_2, self.runner_1)
        self.all_results[3] = tournament3.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3].keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
