class Counter:

    i = 0 # Static => Shared

    @staticmethod
    def count(self):
        Counter.i += 1

if __name__ == '__main__':
    # c1 = Counter()
    # print(c1.i)
    # c1.count()
    # print(c1.i)
    # c2 = Counter()
    # c2.count()
    # print(c2.i)
    Counter.count()