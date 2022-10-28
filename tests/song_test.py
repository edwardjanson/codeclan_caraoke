import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Oh Binary Day")
    
    def test_song_has_name(self):
        self.assertEqual("Oh Binary Day", self.song_1.name)