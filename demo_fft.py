import numpy as np
import matplotlib.pyplot as plt

c1 = 3+2j
c2 = 1j
print(c2 ** 2)
print(c1 * c2)

signal = np.array([0,1,0,0,0,0,0,0,0,0])
plt.plot(signal)
res = np.fft.fft(signal)
print(res)
plt.plot(np.real(res))
plt.show()



