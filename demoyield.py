import intro

def myfilter(fn , l):
    #res = []
    for i in l:
        if fn(i):
            yield i # Return partiel, return streamé
            #res.append(i)
    #return res

def mymap(fn ,l):
    #res = []
    for i in l:
        yield i
        #res.append(fn(i))
    #return res

def myrange(nb):
    i = 0
    while i < nb:
        yield i
        i+=1

def infiniteGenerator():
    i = 0
    while True:
        yield i
        i += 1

l = range(10)
l = infiniteGenerator()
res = myfilter(lambda x : x % 2 == 0, l)
res = myfilter(lambda x : intro.isPrime(x), res)
res = mymap(lambda x : x ** 2, res)
#print(res)
#print(len(res))
#print(res[10])
for i in res: # Boucles intriquées, 2 boucles mais UNE SEULE itération
    print(i)
print("end")
for i in res: # Boucles intriquées, 2 boucles mais UNE SEULE itération
    print(i)
print("end")