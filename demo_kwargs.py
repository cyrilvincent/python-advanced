def my_function(p1, **kwargs):
    print(p1)
    print(kwargs["p2"])
    print(kwargs["p3"])


my_function("p1", p2="toto", p3="titi")

# Rectangle(length, width, x, y) => Rectangle(length, width, Point(x, y))