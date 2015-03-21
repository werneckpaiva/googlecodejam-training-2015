import unittest
from cookie_clicker import CookieClickerRunner


class TestMagicTrickFromFile(unittest.TestCase):

    runner = None

    @classmethod
    def setUpClass(cls):
        cls.runner = CookieClickerRunner('test_cookie_clicker.in')

    def test_answer_1(self):
        self.assertEquals(self.runner.results[0], '1.0000000')

    def test_answer_2(self):
        self.assertEquals(self.runner.results[1], '39.1666667')
 
    def test_answer_3(self):
        self.assertEquals(self.runner.results[2], '63.9680013')
# 
    def test_answer_4(self):
        self.assertEquals(self.runner.results[3], '526.1904762')
