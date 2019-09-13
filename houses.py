import csv
from functools import reduce

with open("house/house.csv") as f:
    reader = csv.DictReader(f)
    gen = (float(row["loyer"]) / float(row["surface"]) for row in reader)
    res = reduce(lambda acc, cur: (acc[0] + cur, acc[1] + 1), gen, (0, 0))
    print(res)
    print(res[0] / res[1])

l = [1,2,3,4,10]
res = reduce(lambda acc, cur : (acc[0]+cur, acc[1]+1), l, (0,0))
print(res)
print(res[0]/res[1])


def reduce2(reduceFn, l, init = 0):
    acc = init
    for cur in l:
        acc = reduceFn(acc, cur)
    return acc


