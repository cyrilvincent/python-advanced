import unittest

def list(l):
    res = []
    for i in l:
        res.append(i)
    return res

class MyTest(unittest.TestCase):

    def testValue(self):
        a = 1
        b = a
        a += 1
        self.assertNotEqual(a, b)

    def testRef(self):
        l1 = [1,2,3]
        l2 = l1
        l1.append(4)
        self.assertEqual(l1, l2)
        self.assertTrue(l1 is l2)
        l3 = list(l1)
        l1.append(5)
        self.assertNotEqual(l1, l3)


if __name__ == '__main__':
    unittest.main()