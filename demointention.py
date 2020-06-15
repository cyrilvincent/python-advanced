l = range(100)

res = [x ** 2 for x in l] # Intention list, Comprehension list
#<=>
res = list(map(lambda x : x ** 2, l))
print(res)

res = [x for x in l if x % 2 == 0]
# <=>
res = list(filter(lambda x : x % 2 == 0, l))
print(res)

res = [x ** 2 for x in l if x % 2 == 0]
# <=>
res = list(map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, l)))
print(res)


# res = []
# for i in l:
#     res.append(i ** 2)
# print(res)