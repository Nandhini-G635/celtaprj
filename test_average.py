import unittest
from average import average

class TestAverage(unittest.TestCase):

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("tearDown")

    
    def test_avg(self):
        out=average([10,10,10])
        self.assertEqual(out, 10.0, "error due to mismatch")

    def test_pass(self):
        out=average([10,10,10])
        self.assertEqual(out, 10.0, "error due to mismatch")

if __name__ == "__main__":
    unittest.main()