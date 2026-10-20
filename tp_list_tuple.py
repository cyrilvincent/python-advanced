# Faire la fonction min_max_avg(l: list[int]) -> tuple[int, int, float] uniquement avec une boucle


def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    """
    Docstring for min_max_avg
    
    :param l: Description
    :type l: list[int]
    :return: Description
    :rtype: tuple[int, int, float]
    """
    sum = 0
    min = l[0]
    max = l[0]
    for value in l:
        sum += value
        if value < min:
            min = value
        elif value > max:
            max = value
    return min, max, sum/len(l)

