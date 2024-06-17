class Counter:

    i = 0 # Static, shared

    def __init__(self):
        Counter.i = 0

    @staticmethod
    def increment():
        Counter.i += 1

    def __del__(self):
        # Destructor
        pass


if __name__ == '__main__':
    c1 = Counter()
    c2 = Counter()
    c1.increment()
    c1.increment()
    c2.increment()
    Counter.increment()
    print(c1.i, c2.i, Counter.i)