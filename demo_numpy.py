import numpy as np
import mylib

a1 = np.array([2,3,4,5,6])
a2 = np.arange(5)
print(a1)
print(a2)
print(a1+a2)
print(a1.size, a1.ndim, a1.shape)

a3 = np.arange(100)
res = a3 % 2 == 0
print(res)

print(a1[[True, False, True, False, True]])
filter = a3 % 2 == 0
print(a3[filter])

f = lambda x: np.sqrt(x) + 1
res = f(a3)
print(res)
