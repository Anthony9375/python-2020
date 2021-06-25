import unittest
from rechteck import Rechteck

class Rechteck_Test(unittest.TestCase):
    def test_rechteck_test(self):
        r = Rechteck(3,5)
        self.assertEqual(r.umfang(), 16)

if __name__ == '__main__':
    unittest.main()