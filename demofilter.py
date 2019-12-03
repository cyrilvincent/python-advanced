import intro

l = range(1000000000000000000000000000000000000000)
# res = intro.filter2(lambda x : x %2 == 0, intro.filter2(intro.isPrime, l))
# for i in res:
#     print(i)

res = filter(lambda x : x %2 == 0, filter(intro.isPrime, l))
res = map(lambda x : x + 1, res)
for i in res:
    print(i)


