from intro import isPrime, isEven, double
l = range(100000000000000000000000000)
#res = filter(isEven, filter(isPrime, l))
res = map(double, filter(isPrime, l))
for i in res:
    print(i)