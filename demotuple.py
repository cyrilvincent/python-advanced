a = 1, 2

def minMaxAvg(l):
    sum = 0
    min = l[0]
    max = l[0]
    for i in l:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max, sum / len(l)

min, max, avg = minMaxAvg(range(1000))
print(min, max, avg)