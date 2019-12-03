def add(x,y):
    return x + y

toto = add

l = [1,2,3,4,5,6,7,8,9]

for val in l:
    print(val)

l[3] = 99
len(l)



print(type(add))
print(toto(3,2))