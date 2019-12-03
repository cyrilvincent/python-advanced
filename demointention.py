import math
l = range(100)
res = list(map(lambda x : math.sin(x / 1000), filter(lambda x : x % 2 == 0, l)))
print(res)

# Intention list
# <=>
res = [math.sin(x / 1000) for x in l if x % 2 == 0]

# Even filter
res = [x for x in l if x % 2 == 0]

# Sinus map
res = [math.sin(x / 1000) for x in l]
