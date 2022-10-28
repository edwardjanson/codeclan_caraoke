import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Billy", 29, 50, "Oh Binary Day")
    
    def test_guest_has_name(self):
        self.assertEqual("Billy", self.guest_1.name)
    
    def test_guest_has_age(self):
        self.guest_1.pay_with_wallet(10)
        self.assertEqual(29, self.guest_1.age)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest_1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Oh Binary Day", self.guest_1.favourite_song)

    def test_guest_can_pay_with_wallet(self):
        self.guest_1.pay_with_wallet(10)
        self.assertEqual(40, self.guest_1.wallet)
    
    def test_guest_cannot_afford(self):
        self.guest_1.pay_with_wallet(60)
        self.assertEqual("Not enough money.", self.guest_1.pay_with_wallet(60))
    
    def test_guest_cheers_if_favourite_song(self):
        self.assertEqual("Woohoo!", self.guest_1.cheer("Oh Binary Day"))