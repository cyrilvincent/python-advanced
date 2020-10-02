import functools

g = range(10)

res = functools.reduce(lambda acc, cur : acc + cur, g,0)
print(res)

# acc = 0
# cur = 0 => 0
# acc = 0
# cur = 1 => 1
# acc = 1
# cur = 2 => 3
# acc = 3
# cur = 3 => 6
# acc = 6
# cur = 4 => 10