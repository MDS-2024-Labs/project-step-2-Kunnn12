import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Character.character import Character
class TestCharacter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Initializing TestCharacter Class")

    @classmethod
    def tearDownClass(cls):
        print("Cleaning TestCharacter Class")

    def setUp(self):
        self.character = Character(name="TestCharacter")

    def tearDown(self):
        del self.character

    def test_initialization(self):
        self.assertEqual(self.character.name, "TestCharacter")
        self.assertIn("HP", self.character.stats)
        self.assertIn("ATK", self.character.stats)
        self.assertIn("CRIT", self.character.stats)
        self.assertIn("DODGE", self.character.stats)
        self.assertEqual(self.character.items, [])

    def test_generate_stats(self):
        stats = self.character.generate_stats()
        self.assertTrue(50 <= stats["HP"] <= 100)
        self.assertTrue(5 <= stats["ATK"] <= 15)
        self.assertTrue(10 <= stats["CRIT"] <= 30)
        self.assertTrue(10 <= stats["DODGE"] <= 30)

    def test_take_damage(self):
        initial_hp = self.character.stats["HP"]
        self.character.take_damage(20)
        self.assertEqual(self.character.stats["HP"], max(0, initial_hp - 20))

    def test_dodge_attack(self):
        result = self.character.dodge_attack(10)
        self.assertIn(result, [True, False])  # Random result

    def test_critical_attack(self):
        result = self.character.critical_attack(10)
        self.assertIn(result, [True, False])  # Random result

