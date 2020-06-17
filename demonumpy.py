import numpy as np
l = [1,2,5,-9,-5,99,8]
a1 = np.array(l)
print(a1)
print(a1 * 2)
print(a1[a1 < 0])
a2 = np.arange(0,0.7,0.1)
print(np.sin(a2))
print(a1 + a2)
print(a1 * a2)
print(np.dot(a1,a2))
print(np.mean(a1), np.max(a1), np.min(a1), np.std(a1), np.var(a1), np.median(a1))

m1 = np.array([[1,2],[3,4]])
v1 = np.array([1,2,3,4])
m1 = v1.reshape(2,2)
print(m1)
print(np.cos(m1) ** 2)
print(np.linalg.inv(m1))

a = 1 + 2j
b = 3 - 4j
print(a + b)
print(1j ** 2)

v1 = [0,1,0,0,0,0,0,0,0,0,0,0,0,0]
mat = np.fft.fft(v1)
import matplotlib.pyplot as plt
plt.plot(np.real(mat))
plt.show()