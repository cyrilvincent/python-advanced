import functools
l = range(1,10)

res = functools.reduce(lambda acc,cur : acc + cur, l)
print(res)