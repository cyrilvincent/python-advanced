from typing import List, Tuple


def min_max_avg(l: List[float]) -> Tuple[float, float, float]:
    sum = l[0]
    min = l[0]
    max = l[0]
    for i in l[1:]:
        sum += i
        if i > max:
            max = i
        if i < min:
            min = i
    return min, max, sum / len(l)

def min_max_avg_dico(l: List[float]) -> Tuple[float, float, float]:
    sum = l[0]
    min = l[0]
    max = l[0]
    for i in l[1:]:
        sum += i
        if i > max:
            max = i
        if i < min:
            min = i
    return {
        "min": min,
        "max": max,
        "avg": sum / len(l)
    }

l = range(10)
min, max, avg = min_max_avg(l)
print(min, max, avg)
res = min_max_avg_dico(l)
print(res["min"], res["max"], res["avg"])
