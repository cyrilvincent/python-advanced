import tp1

def filter_even(l):
    for i in l:
        if i % 2 == 0:
            yield i


def filter_prime(l):
    for i in l:
        if tp1.is_prime(i):
            yield i


def map(l):
    for i in l:
        yield i ** 2


def infinite():
    i = 0
    while True:
        i += 1
        yield i


if __name__ == '__main__':
    l = infinite()
    # res = filter_prime(l)
    # res = filter_even(res)
    # res = map(res)
    res = (x ** 2 for x in l if tp1.is_prime(x))
    for i in res:
        print(f"{i} ", end="")

    [x ** 2 for x in l if tp1.is_prime(x)]
    # <=>
    list((x ** 2 for x in l if tp1.is_prime(x)))


