import math

l = [1,2,5,99,-1,4,88,66,0,88]
print(len(l))
l.append(999)
print(l)
for _ in range(l.count(88)):
    l.remove(88)
print(l)

for value in l:
    print(value)

for i in range(len(l)):
    print(l[i])

for index, value in enumerate(l):
    print(index, value)

identity = [x for x in l]
print(identity)
multiply2 = [x * 2 for x in l]
print(multiply2)

def complex_function(n: int) -> int:
    return n * 2 - 3

result = [complex_function(x) for x in l]
print(result)

result = [x for x in l if x % 2 == 0]
print(result)

def complex_filter(n: int) -> bool:
    return math.cos(n) > 0

result = [x for x in l if complex_filter(x)]
print(result)

result = [x ** 2 for x in l if x % 2 == 0]
print(result)

result = [complex_function(x) for x in l if complex_filter(x)]