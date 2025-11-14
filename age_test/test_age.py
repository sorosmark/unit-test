# python -m unittest test_age -v
import unittest
from age import categorise_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child_age(self):
        self.assertEqual(categorise_by_age(5), "child")
        self.assertEqual(categorise_by_age(5), "child")
        self.assertEqual(categorise_by_age(9), "child")
    
    def test_teenager_age(self):
        self.assertEqual(categorise_by_age(11), "teenager")
        self.assertEqual(categorise_by_age(14), "teenager")
        self.assertEqual(categorise_by_age(18), "teenager")
    
    def test_adult_age(self):
        self.assertEqual(categorise_by_age(20), "adult")
        self.assertEqual(categorise_by_age(32), "adult")
        self.assertEqual(categorise_by_age(65), "adult")
    
    def test_old_age(self):
        self.assertEqual(categorise_by_age(70), "old")
        self.assertEqual(categorise_by_age(66), "old")
        self.assertEqual(categorise_by_age(90), "old")
    
    def test_halfdead_age(self):
        self.assertEqual(categorise_by_age(91), "halfdead")
        self.assertEqual(categorise_by_age(113), "halfdead")
        self.assertEqual(categorise_by_age(120), "halfdead")