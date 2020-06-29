import unittest

l = range(10)
print([x ** 2 for x in l]) #Comprehension list
#<=> MAP + LIST
print(list(map(lambda x : x ** 2, l)))

print([x for x in l if x % 2 == 0])
#<=> FILTER + LIST
print([list(filter(lambda x : x%2 == 0, l))])

print([x ** 2 for x in l if x % 2 == 0])
#<=> MAP + FILTER + LIST
print(list(map(lambda x : x ** 2, filter(lambda x : x % 2 ==0, l))))

class IntentionTest(unittest.TestCase):

    def test1(self):
        l = range(10)
        res1 = [x ** 2 for x in l if x % 2 == 0]
        res2 = list(map(lambda x : x ** 2, filter(lambda x : x % 2 ==0, l)))
        self.assertListEqual(res1, res2)

