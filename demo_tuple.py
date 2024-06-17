def min_max_avg(l: list[float]) -> tuple[float, float, float]:
    """
    Retourner le min, max et avg (len)
    :param l:
    :return:
    """
    min = l[0]
    max = l[0]
    sum = 0
    for val in l:
        sum += val
        if val < min:
            min = val
        if val > max:
            max = val
    return min, max, sum / len(l)


if __name__ == '__main__':
    min, max, avg = min_max_avg(range(10))
    print(min, max, avg)
    v = range(220,230,1)
    a = range(10, 20, 1)
    # calculer p = a * v sans numpy (for + zip)
    p = [volt * amp for volt, amp in zip(v, a)]
    p = [res[0] * res[1] for res in zip(v, a)]
    print(p)
