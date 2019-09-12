# Porter tp1 en lambda + liste en intention
import math
l = range(2000)
res = [x / 1000 for x in l]
res = [math.sin(x) for x in l if math.sin(x) > 0]

def toto():
    return 1,2,3

_,_,c = toto()
print(c)