x = 1
y = x
x += 1
print(x, y, x == y, x is y)
# int float bool str tuple

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l1, l2, l1 == l2, l1 is l2)

l1 = [1, 2, 3]
l2 = list(l1)
l1.append(4)
print(l1, l2, l1 == l2, l1 is l2)