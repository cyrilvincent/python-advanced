import unittest
import tp1

class TP2Test(unittest.TestCase):

    def testPrime(self):
        l = range(100)
        res = filter(tp1.isPrime, l)
        res1 = list(map(lambda x : x ** 2, res))
        res2 = [x ** 2 for x in l if tp1.isPrime(x)]
        self.assertEqual(res1, res2)
        # print(res)
        # for val in res:
        #     print(val)

    def testFilters(self):
        l = range(100)
        res = filter(tp1.isPrime, l)
        res = list(filter(lambda x : x % 2 == 0, res))
        self.assertEqual(2, list(res)[0])
        res = [x for x in l if tp1.isPrime(x)]
        res = [x for x in res if x % 2 == 0]
        # for val in res:
        #     print(val)
        # tp3 refaire tp2 avec des intention list

    def testListReference(self):
        l1 = [1,2,3]
        l2 = l1
        l1.append(4)
        print(l1)
        print(l2)
        self.assertListEqual(l1,l2)
        l2 = list(l1)
        l1.append(4)
        print(l1)
        print(l2)

    def testEqualIs(self):
        l1 = [1,2,3]
        l2 = [1,2,3]
        self.assertListEqual(l1, l2)
        self.assertFalse(l1 is l2)
        l1 = l2
        self.assertListEqual(l1, l2)
        l1.append(4)
        self.assertTrue(l1 is l2)

