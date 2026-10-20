a = 1 # By value
b = a
a += 1
print(a, b)

a = [1, 2] # By ref
b = a
a.append(3)
print(a, b)

a = [1, 2] # By clone
b = list(a)
a.append(3)
print(a, b)

a: list[int] = [1, 2]
b = [1, 2]
print(a == b, a is b)
a = b
print(a == b, a is b)