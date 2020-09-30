import unittest
import demo

class MyTests(unittest.TestCase):

    def test_1(self):
        i = 1
        i += 1
        self.assertEqual(2,i)

    def test_prime_number(self):
        self.assertTrue(demo.is_prime(7))
        self.assertFalse(demo.is_prime(8))
        self.assertFalse(demo.is_prime(1))

if __name__ == '__main__':
    unittest.main()

