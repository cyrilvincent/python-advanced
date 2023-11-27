a = 1
b = a
b += 1
print(a, b, a == b)

a = [1, 2]
b = a # By reference
b.append(3)
print(a, b, a == b, a is b)

a = [1, 2]
b = list(a) # Clone
b.append(3)
print(a, b, a == b, a is b)

print([1,2] == [1,2], [1,2] is [1,2])
a = [1,2]
b = [1,2]
print(a is b)
a = b
print(a is b)
