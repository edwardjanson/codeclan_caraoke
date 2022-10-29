import unittest
from src.karaoke_venue import KaraokeVenue
from src.bar import Bar
from src.drink import Drink
from src.guest import Guest
from src.room import Room

class TestBar(unittest.TestCase):
    
    def setUp(self):
        self.bar = Bar()
        self.drink_1 = Drink("Irn-Bru", 2, False)
        self.drink_2 = Drink("Schiehallion", 6, True)
        self.bar.add_drink(self.drink_1)
        self.bar.add_drink(self.drink_2)

        self.room_1 = Room("Frontstreet Room", 2)
        self.guest_1 = Guest("Billy", 29, 3, "Oh Binary Day")
        self.guest_2 = Guest("Beth", 16, 20, "Smells Like Binary")
    
    def test_bar_has_drinks_list(self):
        self.assertEqual([self.drink_1, self.drink_2], self.bar.drinks_list)
        
    def test_add_drink(self):
        self.bar.add_drink(Drink("Leffe", 5, True))
        self.assertEqual(3, len(self.bar.drinks_list))
    
    def test_sell_alcoholic_drink(self):
        self.assertEqual("Cheers.", self.bar.sell_drink(self.guest_2, self.room_1, self.drink_1))
    
    def test_sell_alcoholic_drink_and_too_young(self):
        self.assertEqual("Too young.", self.bar.sell_drink(self.guest_2, self.room_1, self.drink_2))
    
    def test_sell_alcoholic_drink_not_enough_money(self):
        self.assertEqual("That's not enough money.", self.bar.sell_drink(self.guest_1, self.room_1, self.drink_2))