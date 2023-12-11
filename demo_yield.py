import rappels
l = range(1000000000000000000000000000000000000000000000000000)

res = (x for x in l if rappels.is_prime(x))
res = (x for x in res if x % 2 == 0)
for i in res:
    print(i)

