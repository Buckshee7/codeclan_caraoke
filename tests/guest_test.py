from classes.guest import Guest
import unittest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Tim", 32)

    def test_guest_has_name(self):
        self.assertEqual("Tim", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(32, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(float, type(self.guest.wallet))