import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Character.player import Player

class TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Initializing TestPlayer Class")

    @classmethod
    def tearDownClass(cls):
        print("Cleaning TestPlayer Class")

    def setUp(self):
        self.player = Player()

    def tearDown(self):
        del self.player

    def test_initialization(self):
        self.assertEqual(self.player.name, "Player")
        self.assertIn("HP", self.player.stats)

    def test_use_item(self):
        item = {"name": "Health Potion", "effect": {"HP": 20}}
        initial_hp = self.player.stats["HP"]
        self.player.use_item(item)
        self.assertEqual(self.player.stats["HP"], min(100, initial_hp + 20))

    def test_choose_attack(self):
        attack = self.player.choose_attack("1")
        self.assertEqual(attack["attack_type"], "Basic Attack")
        self.assertTrue(attack["damage"] > 0)

        attack = self.player.choose_attack("2")
        self.assertEqual(attack["attack_type"], "Heavy Strike")

        attack = self.player.choose_attack("3")
        self.assertEqual(attack["attack_type"], "Quick Attack")

        # Test invalid input defaults to Basic Attack
        attack = self.player.choose_attack("invalid")
        self.assertEqual(attack["attack_type"], "Basic Attack")

