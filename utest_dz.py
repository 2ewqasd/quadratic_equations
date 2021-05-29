import unittest
import dz


class DzTest(unittest.TestCase):
    def test_first(self):
        self.assertEqual(dz.first_case(3,-14,256), (5.0, -0.3333333333333333))

    def test_second(self):
        self.assertEqual(dz.second_case(4,-20),(2.5,2.5))
    
    def test_fifth(self):
        self.assertEqual(dz.fifth_case(4,-64),(4,-4))
    
    def test_sixth(self):
        self.assertEqual(dz.sixth_case(4,12),(0,-3))

if __name__ == '__main__':
    unittest.main()