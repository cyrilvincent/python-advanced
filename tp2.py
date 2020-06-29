import unittest
import tp1

class TP2Test(unittest.TestCase):

    def testPrime(self):
        l = range(100000)
        res = filter(tp1.isPrime, l)
        res = list(map(lambda x : x ** 2, res))
        # print(res)
        # for val in res:
        #     print(val)

    def testFilters(self):
        l = range(100)
        res = filter(tp1.isPrime, l)
        res = list(filter(lambda x : x % 2 == 0, res))
        self.assertEqual(2, list(res)[0])
        # for val in res:
        #     print(val)
        # tp3 refaire tp2 avec des intention list

