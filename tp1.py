import sys
print(sys.version)

def is_prime(x: int) -> bool:
    """
    Détecte si x est premier
    :param x: le nombre entier à tester
    :return: vrai si x est premier, x est premier ssi il possède exactement 2 diviseurs 1 et lui même
    Tout nombre > 1 est premier sauf s'il possède un diviseur entre 2 et x-1
    """
    pass

def filter_primes(l: list[int]) -> list[int]:
    """
    Filter la liste l uniquement sur les nombre premiers
    :param l: la liste à filtrer
    :return: la liste filtrée
    ex: filter_primes([1,2,3,4,5,6,7,8,9]) -> [2,3,5,7]
    """

if __name__ == '__main__':
    print(is_prime(7)) # True

