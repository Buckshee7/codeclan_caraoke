from classes.bartab import Bartab
import unittest

class TestBartab(unittest.TestCase):
    def setUp(self):
        self.tab = Bartab()

    def test_bartab_init(self):
        self.asserEqual(0, self.tab.total)
        self.asserEqual(list, type(self.tab.history))
