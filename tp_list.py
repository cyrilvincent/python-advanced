import math

l = [1,2,5,99,-1,4,88,66,0,88]
# Avec une liste en intention faire
#   Appliquer un cos
#   Filtrer le nb impairs
#   cos + impair
# Créer la fonction is_prime(nb: int) -> bool : réciproque = Tout nb >=2 est premier sauf s'il possède un diviseur entre 2 et nb-1
# Fitlrer l sur les nb premier puis les mettre au carré

result = [math.cos(x) for x in l]
result = [x for x in l if x % 2 == 1]
result = [math.cos(x) for x in l if x % 2 == 1]
print(result)

def is_prime(nb: int) -> bool:
    if nb < 2:
        return False
    for div in range(2, nb):
        if nb % div == 0:
            return False
    return True
    
print(is_prime(7), is_prime(7919))

result = [x ** 2 for x in l if is_prime(x)]
print(result)