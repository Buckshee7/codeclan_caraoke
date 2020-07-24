from classes.guest import Guest
from classes.song import Song
import unittest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Don't Stop Believin'", "Journey")
        self.guest = Guest("Tim", 32, 20.5, self.song)

    def test_guest_has_name(self):
        self.assertEqual("Tim", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(32, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(20.5, self.guest.wallet)

    def test_guest_has_no_fav_song_if_not_provided(self):
        guest_no_fav = Guest("Bob", 60, 100)
        self.assertEqual(None, guest_no_fav.fav_song)

    def test_guest_has_fav_song_if_provided(self):
        self.assertEqual(self.song, self.guest.fav_song)

    def test_guest_wallet_reduction(self):
        self.guest.reduce_wallet(5)
        self.assertEqual(15.5, self.guest.wallet) 