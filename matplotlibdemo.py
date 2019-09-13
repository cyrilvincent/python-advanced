import matplotlib.pyplot as plt
import math

l = [math.sin(x / 500) for x in range(4000)]

plt.subplot(221)
plt.plot(range(4000), l)
plt.subplot(222)
plt.plot(range(4000))
plt.subplot(223)
plt.bar(range(10),height=10)
plt.show()

# x = surface, y = loyer

