import unittest
from src.karaoke_venue import KaraokeVenue
from src.room import Room
from src.guest import Guest
from src.bar import Bar

class TestKaraokeVenue(unittest.TestCase):
    
    def setUp(self):
        self.karaoke_bar = KaraokeVenue("Binary Tunes", 2000)

        self.room_1 = Room("The Onspring Room", 2)
        self.room_2 = Room("Green Mild Chili Room", 8)
        self.karaoke_bar.add_room(self.room_1)
        self.karaoke_bar.add_room(self.room_2)

        self.guest_1 = Guest("Billy", 29, 50, "Oh Binary Day")
        self.guest_2 = Guest("Eilidh", 29, 8, "Smells Like Binary")
    
    def test_karaoke_venue_has_name(self):
        self.assertEqual("Binary Tunes", self.karaoke_bar.name)
    
    def test_karaoke_venue_has_till(self):
        self.assertEqual(2000, self.karaoke_bar.till)
    
    def test_add_money_to_till(self):
        self.karaoke_bar.increase_till(10)
        self.assertEqual(2010, self.karaoke_bar.till)

    def test_karaoke_venue_has_entry_fee(self):
        self.assertEqual(10, self.karaoke_bar.entry_fee)

    def test_add_room(self):
        self.room_3 = Room("Frontstreet Room", 5)
        self.karaoke_bar.add_room(self.room_3)
        self.assertEqual(3, len(self.karaoke_bar.rooms))
    
    def test_add_bar(self):
        self.bar = Bar()
        self.karaoke_bar.add_bar(self.bar)
        self.assertNotEqual(None, self.bar)
    
    def test_guest_can_pay_entry_fee_and_there_is_room(self):
        self.karaoke_bar.get_entry_fee(self.guest_1, self.room_1)
        self.assertEqual(1, len(self.room_1.guests))
    
    def test_guest_cannot_pay_entry_fee_and_there_is_room(self):
        self.karaoke_bar.get_entry_fee(self.guest_2, self.room_1)
        self.assertEqual(0, len(self.room_1.guests))
    
    def test_guest_can_pay_entry_fee_but_there_is_no_room(self):
        self.karaoke_bar.check_in_guest(self.guest_1, self.room_1)
        self.karaoke_bar.check_in_guest(self.guest_2, self.room_1)
        self.karaoke_bar.get_entry_fee(self.guest_1, self.room_1)
        self.assertEqual(2, len(self.room_1.guests))

    def test_check_in_guest(self):
        self.guest_2 = Guest("Eilidh", 27, 40, "Smells Like Binary")
        self.karaoke_bar.check_in_guest(self.guest_2, self.room_1)
        self.assertEqual(2, len(self.room_1.guests))

    def test_check_out_guest(self):
        self.karaoke_bar.check_out_guest(self.guest_1, self.room_1)
        self.assertEqual(0, len(self.room_1.guests))
    
    def test_refuse_check_in_if_capacity_is_reached(self):
        self.guest_2 = Guest("Eilidh", 27, 30, "Smells Like Binary")
        self.karaoke_bar.check_in_guest(self.guest_2, self.room_1)
        self.guest_3 = Guest("Henry", 20, 35, "Hey Dude")
        self.assertEqual("Sorry, this room is full.", self.karaoke_bar.check_in_guest(self.guest_3, self.room_1))

    def test_get_tab_value(self):
        self.room_1.increase_tab(20, self.guest_1)
        self.room_2.increase_tab(50, self.guest_2)
        self.assertEqual(70, self.karaoke_bar.tab_value())
