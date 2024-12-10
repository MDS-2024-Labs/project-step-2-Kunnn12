import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Character.player import Player
from Gameplay.events import generate_event, handle_event

class TestEvents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Initializing TestEvents Class")

    @classmethod
    def tearDownClass(cls):
        print("Cleaning TestEvents Class")

    def setUp(self):
        self.player = Player()

    def tearDown(self):
        del self.player

    def test_generate_event(self):
        event = generate_event()
        self.assertTrue(isinstance(event, str), "Event should be a string")
        self.assertGreater(len(event), 0, "Event should not be empty")

    def test_handle_event(self):
        initial_hp = self.player.stats["HP"]
        handle_event(self.player)
        self.assertTrue(self.player.stats["HP"] != initial_hp, "Event should affect player's HP")
        self.assertTrue(len(self.player.items) >= 0, "Player should have items or none")
