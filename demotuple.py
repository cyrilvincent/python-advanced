def fonctionquiretourneplusieursvaleurs():
    return 1,True,3.14,"toto"

import unittest
class TupleTest(unittest.TestCase):

    def test1(self):
        res = fonctionquiretourneplusieursvaleurs()
        print(res)
        self.assertEqual((1,True,3.14,"toto"), res)
        self.assertEqual(res[0],1)
        self.assertEqual(res[-1], "toto")

    def test2(self):
        (a,_,_,d) = fonctionquiretourneplusieursvaleurs()
        self.assertEqual(a, 1)
        self.assertEqual(d, "toto")

    def test3(self):
        a,_,_,d = fonctionquiretourneplusieursvaleurs()
        self.assertEqual(a, 1)
        self.assertEqual(d, "toto")

