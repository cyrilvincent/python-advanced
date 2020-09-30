def is_prime(x):
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
    return True

def filter_even(l):
    res = []
    for i in l:
        if i % 2 == 0:
            res.append(i)
    return res

def myfilter(fn, l):
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res

def mymap(fn, l):
    res = []
    for i in l:
        res.append(fn(i))
    return res

def double(x):
    return x * 2

def inc(x):
    return x + 1

def demo_tuple():
    #Calcul
    a = 1
    b = 99
    return a,b

def min_max_avg(l):
    min = l[0]
    max= l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        elif i > max:
            max = i
        sum += i
    return min, max, sum / len(l)

def min_max_avg_dico(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        elif i > max:
            max = i
        sum += i
    return {"min":min, "max":max, "avg":sum / len(l)}

def dico():
    dico = {
        "author": "Hans Christian Andersen",
        "country": "Denmark",
        "imageLink": "images/fairy-tales.jpg",
        "language": "Danish",
        "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
        "pages": 784,
        "title": "Fairy tales",
        "year": 1836
    }
    return dico




# Reprise 10h35
