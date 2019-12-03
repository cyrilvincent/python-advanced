volts = [220.0,220.1,220.2,221,222]
amperes = [10.0,10.1,9.9,10.3,11]
t = [0,1,2,3,4]
print(list(zip(t, volts, amperes)))

res = [u * i for u,i in zip(volts, amperes)]
print(res)
