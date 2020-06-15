import intro

l = range(100000000000000000000000000000000000000)

res = (x ** 2 for x in l if x % 2 == 0)
# <=>
res = map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, l))


res = (x for x in l if x % 2 == 0)
res = (x for x in res if intro.isPrime(x))

for i in res:
    print(i)
