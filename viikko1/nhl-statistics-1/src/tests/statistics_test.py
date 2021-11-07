import unittest
from statistics import Statistics
from player import Player

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
        self.statistics = Statistics(
            PlayerReaderStub()
        )
        
    
    def test_search_player(self):
        player_found = self.statistics.search("Semenko")
        self.assertEqual(player_found.name, "Semenko")
    
    def test_search_player_not_found(self):
        player_found = self.statistics.search("this is not a name")
        self.assertEqual(player_found, None)

    def test_team_players(self):
        list_of_players = self.statistics.team("EDM")
        self.assertEqual(len(list_of_players), 3)
        self.assertEqual(list_of_players[0].name, "Semenko")
        self.assertEqual(list_of_players[1].name, "Kurri")
        self.assertEqual(list_of_players[2].name, "Gretzky")
    
    def test_top_scorers(self):
        list_of_scorers = self.statistics.top_scorers(3)
        self.assertEqual(len(list_of_scorers), 3)
        self.assertEqual(list_of_scorers[0].name, "Gretzky")
        self.assertEqual(list_of_scorers[1].name, "Lemieux")
        self.assertEqual(list_of_scorers[2].name, "Yzerman")