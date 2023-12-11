a = 1
b = a
a += 1
print(a, b)

a = [1, 2]
b = a
a.append(3)
print(a, b)

a = [1, 2]
b = list(a) # Cloned
a.append(3)
print(a, b)

a = [1, 2]
b = [1, 2]
print(a == b, a is b)
a = b
print(a == b, a is b)