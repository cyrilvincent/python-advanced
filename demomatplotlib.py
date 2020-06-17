import matplotlib.pyplot as plt
import math
f = lambda x : math.sin(x)
x = range(100)
y = [f((i * 2 * math.pi)/100) for i in x]
plt.plot(x,y) #plot relie les points, scatter non relié, bar
plt.yscale('log')
#plt.axis([0.0,100,-2.0,2.0])
plt.show()