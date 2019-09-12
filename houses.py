import csv

with open("house/house.csv") as f:
    reader = list(csv.DictReader(f))
    print(sum([float(row["loyer"]) / float(row["surface"]) for row in reader]) / len(reader))

    l = range(5)
    print(sum(l))
from functools import reduce
print(reduce(lambda acc, cur : acc + cur, l ))

def reduce2(reduceFn, l, init = 0):
    acc = init
    for cur in l:
        acc = reduceFn(acc, cur)
    return acc


