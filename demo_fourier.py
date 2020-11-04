import numpy as np
import matplotlib.pyplot as plt

signal = [0,1.0,0,0,0,0,0,0,0,0]
plt.subplot(211)
plt.plot(range(len(signal)), signal)
mat = np.fft.fft(signal)
print(mat)
plt.subplot(212)
plt.plot(np.real(mat))
plt.show()
