import unittest
from statistics import Statistics
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_name(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")

    def test_search_returns_none(self):
        self.assertEqual(self.statistics.search("AAA"), None)
    
    def test_team_returns_list(self):
        statistics_team_list = self.statistics.team("EDM")
        self.assertEqual(len(statistics_team_list), 3)

    def test_top_returns_top_player_points(self):
        self.assertEqual(self.statistics.top(1, SortBy.POINTS)[0].name, "Gretzky")

    def test_top_returns_top_player_goals(self):
        self.assertEqual(self.statistics.top(1, SortBy.GOALS)[0].name, "Lemieux")
    
    def test_top_returns_top_player_assists(self):
        self.assertEqual(self.statistics.top(1, SortBy.ASSISTS)[0].name, "Gretzky")