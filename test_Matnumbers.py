import unittest
from Matnumbers import adding

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(adding(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(adding(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(adding(1, -2), -1)
        self.assertEqual(adding(-1, 2), 1)
    
    def test_less(self):
        a=10
        b=20
        self.assertLess(a,b)
    
    
    def test_great(self):
        a=40
        b=20
        self.assertGreater(a,b)

if __name__ == '__main__':
    unittest.main()