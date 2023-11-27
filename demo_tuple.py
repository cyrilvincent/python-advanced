from typing import List, Tuple, Dict


def min_max_avg(l: List[float]) -> Tuple[float, float, float]:
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    return min, max, sum / len(l)

def min_max_avg_dico(l: List[float]) -> Dict[str, float]:
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    return {"min": min, "max": max, "avg": sum/len(l)}


if __name__ == '__main__':
    l = [1, 3, 8, 99, 100, 10, 13, 17, 2, 18]
    min, max, avg = min_max_avg(l)
    print(min, max, avg)
    dico = min_max_avg_dico(l)
    print(dico)