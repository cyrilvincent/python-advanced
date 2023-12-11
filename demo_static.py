class Counter:

    # static Shared between instances
    i = 0

    def __init__(self):
        pass

    @staticmethod
    def increment():
        Counter.i += 1



if __name__ == '__main__':
    c1 = Counter()
    print(c1.i)
    c1.increment()
    print(c1.i)
    c1.increment()
    print(c1.i)
    c2 = Counter()
    c2.increment()
    Counter.increment()
    print(c2.i)