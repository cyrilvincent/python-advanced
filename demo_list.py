l = [1,2,3,4,5,6,7,8,9,10]

res = [x ** 2 for x in l if x % 2 == 0]
print(res)

a: int = 1
b: int = a
a += 1
print(a, b)

a: list[int] = [1, 2]
b: list[int] = a
a.append(3)
print(a, b)

a: list[int] = [1, 2]
b: list[int] = list(a) # clone
a.append(3)
print(a, b)

a = [1, 2]
b = [1, 2]
print(a == b, a is b)
a = b
print(a == b, a is b)