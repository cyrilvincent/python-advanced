from typing import List


def is_prime(nb: int) -> bool:
    """
    Is prime number
    :param nb: nb to test
    :return: True if nb is prime number
    """
    if nb < 2:
        return False
    for div in range(2, nb):
        if nb % div == 0:
            return False
    return True


def filter_prime(l: List[int]) -> List[int]:
    res = []
    for value in l:
        if is_prime(value):
            res.append(value)
    return res


if __name__ == '__main__':
    print(is_prime(7))
    print(is_prime(2))
    print(is_prime(8))

