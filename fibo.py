import functools
import time

# Recursive
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)
print(fibo(10))

# Yield
def fibo(n):
    n1 = 1
    n2 = 0
    while n > 1:
        sum = n1 + n2
        n2 = n1
        n1 = sum
        n -= 1
        yield sum
        time.sleep(1)

res = fibo(10)
for i in res:
    print(i)

#Reduce
fibo = lambda x, _ : (x[0] + x[1], x[0]) #(x[0]=n-1, x[1]=n-2)
n = 10
res = functools.reduce(fibo,range(1, n),(1,0))
print(res[0])


