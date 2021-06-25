import unittest
from person import Person

class person_test(unittest.TestCase):
    def test_name(self):
        p = Person("Alex", 30)
        self.assertEqual(p.get_name(), "Alex")

    def test_age(self):
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()