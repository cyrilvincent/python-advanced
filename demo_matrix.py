import numpy as np
m1 = np.array([[1,2], [3,4]])
print(m1)
print(np.tanh(m1))
print(m1 + np.tanh(m1))

print(m1.shape)

v1 = np.arange(12)
print(v1, v1.shape)
m2 = v1.reshape(3,-1)
print(m2, m2.shape)

print(np.linalg.inv(m1))
