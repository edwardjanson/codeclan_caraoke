import unittest
from src.karaoke_venue import KaraokeVenue
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.karaoke_bar = KaraokeVenue("Binary Tunes", 2000)

        self.room_1 = Room("Frontstreet Room", 2)
        self.guest_1 = Guest("Billy", 29, 50, "Oh Binary Day")
        self.song_1 = Song("Hey Dude")
        self.karaoke_bar.check_in_guest(self.guest_1, self.room_1)
        self.room_1.add_song(self.song_1)

    def test_room_has_name(self):
        self.assertEqual("Frontstreet Room", self.room_1.name)

    def test_room_has_space(self):
        self.assertEqual(True, self.room_1.has_space())
    
    def test_room_has_no_space_left(self):
        self.guest_2 = Guest("Eilidh", 27, 30, "Smells Like Binary")
        self.karaoke_bar.check_in_guest(self.guest_2, self.room_1)
        self.assertEqual(False, self.room_1.has_space())
    
    def test_room_has_capacity_number(self):
        self.assertEqual(2, self.room_1.capacity)
    
    def test_room_has_songs_list(self):
        self.assertEqual([self.song_1], self.room_1.songs)
    
    def test_room_has_guests_list(self):
        self.assertEqual([self.guest_1], self.room_1.guests)
    
    def test_room_has_tab(self):
        self.assertEqual({}, self.room_1.tab)
    
    def test_add_song(self):
        self.song_2 = Song("Smells Like Binary")
        self.room_1.add_song(self.song_1)
        self.assertEqual(2, len(self.room_1.songs))

    def test_increase_tab(self):
        self.room_1.increase_tab(10, self.guest_1)
        self.assertEqual(10, self.room_1.tab)
