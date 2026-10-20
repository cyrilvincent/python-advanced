"""
Docstring for hello
"""
import sys

print("Hello")
print(sys.version)

x = 3
for i in range(10):
    if i % 2 == 0:
        print("Pair")


def is_even(n:int) -> bool:
    """
    Blah blah
    :param n: Description
    :type n: int
    :return: Description
    :rtype: bool
    """
    return n % 2 == 0

print(is_even(4.1))
print(is_even(n=4))

