import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.test_character import TestCharacter
from tests.test_npc import TestNPC
from tests.test_player import TestPlayer

def my_suite():
    suite = unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(TestCharacter))
    suite.addTest(unittest.makeSuite(TestNPC))
    suite.addTest(unittest.makeSuite(TestPlayer))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

if __name__ == "__main__":
    my_suite()
