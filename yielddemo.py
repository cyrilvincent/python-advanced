import math

def isPrime(x:int):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def filter2(predicatFn, l):
    for i in l:
        if predicatFn(i):
            yield i

def map2(mapFn, l):
    for i in l:
        yield mapFn(i)

#res = filter2(lambda x : x % 2 == 0, range(100))
#res = filter2(isPrime, res)
res = filter2(isPrime, range(100))
#res = list(res)
res = map2(math.sqrt, res)

# res = map(lambda x : x **2, filter(lambda x : x % 2 == 0, range(100)))
# # <=> Generator
# res = (x **2 for x in range(100) if x % 2 == 0)
# # In memory
# res = list((x **2 for x in range(100) if x % 2 == 0))
# # <=> Generateur + List <=> Liste en intention
# res = [x **2 for x in range(100) if x % 2 == 0]

def infiniteYield():
    i = 0
    while(True):
        i += 1
        yield i


#
# Lazy Loading
for i in res:
    print(i)



