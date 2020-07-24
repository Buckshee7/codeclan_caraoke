from classes.song import Song
import unittest

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Don't Stop Believin'", "Journey")

    def test_song_has_title(self):
        self.assertEqual("Don't Stop Believin'", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Journey", self.song.artist)