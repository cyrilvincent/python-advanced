def is_even(x:int)->bool:
    return x % 2 == 0

def is_prime(x:int)->bool:
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
        return True

def complex_function(a,b,*kargs,**kwargs):
    print(a,b)
    for item in kargs:
        print(item)
    for key in kwargs.keys():
        print(f"{key}:{kwargs[key]}")