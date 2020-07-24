from classes.bartab import Bartab
import unittest

class TestBartab(unittest.TestCase):
    def setUp(self):
        self.tab = Bartab()

    def test_bartab_init(self):
        self.assertEqual(0, self.tab.total)
        self.assertEqual(list, type(self.tab.history))

    def test_bartab_increase(self):
        self.tab.increase_total(10)
        self.assertEqual(10, self.tab.total)