def test_tuple():
    return 1, "toto", 0, "x"

a,b,_,_ = test_tuple()
print(a,b)

# faire la fonction min_max_avg(generator)->Tuple[float, float, float]