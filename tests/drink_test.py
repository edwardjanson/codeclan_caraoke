import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("Leffe", 5, True)
        self.drink_2 = Drink("Irn-Bru", 2, False)
    
    def test_drink_has_name(self):
        self.assertEqual("Leffe", self.drink_1.name)
        
    def test_drink_has_price(self):
        self.assertEqual(5, self.drink_1.price)

    def test_drink_has_alcohol(self):
        self.assertEqual(True, self.drink_1.has_alcohol)
    
    def test_drink_has_no_alcohol(self):
        self.assertEqual(False, self.drink_2.has_alcohol)
