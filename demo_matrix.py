import numpy as np

m1 = np.array([[1,2],[3,4]])
print(m1 * 2)
print(np.sin(m1))

print(np.linalg.inv(m1))

print(m1.size, m1.shape)

v1 = np.arange(12)
m2 = v1.reshape(4,-1)
print(m2)
m3 = v1.reshape(4,3)
print(m3)
