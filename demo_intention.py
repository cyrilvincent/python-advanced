l = [1,3,8,99,100,10,13,17,2,18]

res = [x * 2 for x in l]
print(res)

res = [x for x in l if x % 2 == 0]
print(res)

res = [x * 2 for x in l if x % 2 == 0]
print(res)