from classes.bartab import Bartab
from classes.guest import Guest
import unittest

class TestBartab(unittest.TestCase):
    def setUp(self):
        self.tab = Bartab()
        self.guest = Guest("Tim", 32, 20.5)

    def test_bartab_init(self):
        self.assertEqual(0, self.tab.total)
        self.assertEqual(list, type(self.tab.receipt))

    def test_bartab_increase(self):
        self.tab.increase_total(10)
        self.assertEqual(10, self.tab.total)

    def test_add_receipt_item(self):
        self.tab.add_receipt_item(self.guest, "Entry Fee", 10)
        self.assertEqual([{"Customer":"Tim", "Sale Item":"Entry Fee", "Value":10}], self.tab.receipt)