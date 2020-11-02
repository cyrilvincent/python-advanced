import tp1

def remove_all(l, item):
    nb = l.count(item)
    for _ in range(nb):
        l.remove(item)
    return l

def remove_all2(l, item):
    res =[]
    for i in l:
        if i != item:
            res.append(i)
    return res

def filter_even(l):
    res = []
    for i in l:
        if tp1.is_even(i):
            res.append(i)
    return res

def filter_prime(l):
    res = []
    for i in l:
        if tp1.is_prime(i):
            res.append(i)
    return res