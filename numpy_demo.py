import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.ones(4) # [1,1,1,1]
a3 = np.array([5,6,7,8])
print(a1 + 1)
print(a1 + a2)
print(a1.__add__(a2))
print(type(a1))

print(a1 * 2)
print(a1 * a3)
print(np.dot(a1, a3))
print(a1.dot(a3))

print(a1 <= 2)
print(a1[2])
print(a1[[True,False,True,False]])
print(a1[a1 <= 2])

f = lambda x : x + 1
print(f(a1))

feven = lambda x : x % 2 == 0
print(feven(a1))
print(a1[feven(a1)])
a4 = a1[feven(a1)]

print(a1.shape)
print(a1.ndim)

m1 = np.array([[1,2,3],[3,4,5]])
print(m1)
print(m1.ndim)
print(m1.shape) #row first
print(m1.T)
print(m1[feven(m1)])

m2 = a1.reshape(2,2)
print(m2)
print(1 / m2)
print(np.linalg.inv(m2))
print(m2 + 1)

print(np.mean(a1))
print(m2)
print(np.mean(m2, axis=1))

m3 = np.append(m2,[[4,5]],axis=0)
m4 = np.append(m2.reshape(4),[4,5]).reshape(3,2)
print(m3)
print(m4)


