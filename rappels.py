from typing import List


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for div in range(2, x):
        if x % div == 0:
            return False
    return True


def sum(l: List[int]) -> int:
    total = 0
    for value in l:
        total += value
    return total


def filter_even(l: List[int]) -> List[int]:
    res = []
    for value in l:
        if value % 2 == 0:
            res.append(value)
    return res


def filter_prime(l: List[int]) -> List[int]:
    res = []
    for value in l:
        if is_prime(value):
            res.append(value)
    return res


if __name__ == '__main__':
    print(is_prime(7))
    print(is_prime(9))
    l = [1,2,8,7,9,12,13,99,51,11]
    print(sum(l))
    print(filter_even(l))
    print(filter_prime(l))
