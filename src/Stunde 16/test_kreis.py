import unittest
from kreis import Kreis

class Kreis_test(unittest.TestCase):

    def test_umfang(self):
        k = Kreis(3)
        self.assertEqual(k.umfang(), 12.5663704)

    def test_flaeche(self):
        k = Kreis
        self.assertEqual(k.flaeche(), 12.5663704)

if __name__=='__main__':
    Kreis_test.main()