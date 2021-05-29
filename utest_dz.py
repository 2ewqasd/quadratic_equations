import unittest
import dz


class DzTest(unittest.TestCase):
    def test(self):
        self.assertEqual(dz.decision(3,-14,-5), (5.0, -0.3333333333333333)) # D > 0
        self.assertEqual(dz.decision(4,-20,25), (2.5, 2.5)) # D = 0
        self.assertEqual(dz.decision(-3,0,75), (5, -5)) # b = 0
        self.assertEqual(dz.decision(4,12,0), (0, -3)) # c = 0 
        self.assertEqual(dz.decision(1,0,0), (0, 0)) # b = 0, c = 0

    

if __name__ == '__main__':
    unittest.main()