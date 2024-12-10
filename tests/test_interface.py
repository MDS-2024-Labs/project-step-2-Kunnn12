import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Gameplay.interface import display_stats
from Character.player import Player

class TestInterface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Initializing TestInterface Class")

    @classmethod
    def tearDownClass(cls):
        print("Cleaning TestInterface Class")

    def setUp(self):
        self.player = Player()

    def tearDown(self):
        del self.player

    def test_display_stats(self):
        try:
            display_stats(self.player)
        except Exception as e:
            self.fail(f"display_stats raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
