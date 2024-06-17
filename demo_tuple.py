def min_max_avg(l: list[float]) -> tuple[float, float, float]:
    """
    Retourner le min, max et avg (len)
    :param l:
    :return:
    """
    return 0., 10., 5.

if __name__ == '__main__':
    min, max, avg = min_max_avg([1,2,3])
    print(min, max, avg)
    v = range(220,230,1)
    a = range(10, 20, 1)
    # calculer p = a * v sans numpy (for + zip)
