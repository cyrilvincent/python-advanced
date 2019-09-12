import unittest

def minMaxAvg(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        elif i > max:
            max = i
        sum += i
    return min, max, sum / len(l)

class MyTests(unittest.TestCase):

    def testTp(self):
        l = [-2,0,5,9,-99,99,6,7,12]
        print(l)
        min, max, avg = minMaxAvg(l)
        self.assertEqual(-99, min)
        self.assertEqual(99, max)
        self.assertAlmostEqual(4.11111, avg, delta=1e-5)

    def testZip(self):
        ts = [0,1,2,3,4,5]
        volts = [220,221,222,23,224,225]
        amps = [3.2,3.1,3.0,2.9,2.8,2.7]
        self.assertEqual((0,220,3.2), list(zip(ts,volts,amps))[0])
        res = [(t, u * i) for t,u,i in zip(ts,volts,amps) if ts > 10]
        self.assertEqual((0,220*3.2), res[0])

