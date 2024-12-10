import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Character.player import Player
from Character.npc import NPC
from Gameplay.combat import execute_player_turn, execute_npc_turn, start_combat

class TestCombat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Initializing TestCombat Class")

    @classmethod
    def tearDownClass(cls):
        print("Cleaning TestCombat Class")

    def setUp(self):
        self.player = Player()
        self.npc = NPC()

    def tearDown(self):
        del self.player
        del self.npc

    def test_player_turn_execution(self):
        execute_player_turn(self.player, self.npc)
        self.assertTrue(self.npc.stats["HP"] <= 100, "NPC HP should decrease or remain unchanged")

    def test_combat_loop(self):
        start_combat(self.player, self.npc)
        self.assertTrue(self.player.stats["HP"] == 0 or self.npc.stats["HP"] == 0, "One character should have 0 HP")
