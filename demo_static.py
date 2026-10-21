class Counter:

    i = 0
    
    def increment(self):
        Counter.i += 1

    @staticmethod
    def increment2():
        Counter.i += 1


class Singleton:

    instance = None

    @staticmethod
    def factory():
        if Singleton.instance is None:
            Singleton.instance = Singleton()
        return Singleton.instance
    



c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
c2.increment()
Counter.increment2()
print(c1.i, c2.i, Counter.i)

s1 = Singleton.factory()
print(s1)
s2 = Singleton.factory()
print(s2)
print(s1 is s2)

toto = 3.14
print(f"Les resultat est {toto:.2f}")