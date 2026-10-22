def is_prime(nb: int) -> bool:
    if nb < 2:
        return False
    for div in range(2, nb):
        if nb % div == 0:
            return False
    return True

l = range(100000000000000000000000000000000000000000)
# result = []
# for value in l:
#     if is_prime(value):
#         result.append(value)



def filter_prime(l: list[int]) -> list[int]:
    result = []
    for value in l:
        if is_prime(value):
            result.append(value)
    return result

def filter_prime_yield(l: list[int]):
    for value in l:
        if is_prime(value):
            yield value

def infinite():
    i = 0
    while True:
        yield i
        i += 1

def range(max: int):
    i = 0
    while i < max:
        yield i
        i += 1

# result = (v for v in l if is_prime(v))  # Generator
result = filter_prime_yield(infinite())
result2 = (v for v in result if v % 2 == 0)
result2[1000]
for v in result:
    print(v)