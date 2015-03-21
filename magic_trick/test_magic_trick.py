import unittest
from magic_trick import MagicTrickRunner


class TestMagicTrickFromFile(unittest.TestCase):

    runner = None

    @classmethod
    def setUpClass(cls):
        cls.runner = MagicTrickRunner('test_magic_trick.in')

    def test_right_answer(self):
        self.assertEquals(self.runner.results[0], 7)

    def test_bad_magician(self):
        self.assertEquals(self.runner.results[1], "Bad magician!")

    def test_volunteer_cheated(self):
        self.assertEquals(self.runner.results[2], "Volunteer cheated!")
