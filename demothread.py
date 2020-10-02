import time
import threading
import subprocess

class MyClass(threading.Thread):

    staticvar = 0
    mylock = threading.RLock()

    def __init__(self, i, nb, fn, endfn):
        super().__init__()
        self.res = None
        self.nb = nb
        self.fn = fn
        self.endfn = endfn
        self.i = i

    def huge(self, nb = 100):
        res = 1
        for _ in range(nb):
            time.sleep(0.1)
            res *= 2
            with MyClass.mylock:
                self.fn(self.i, res)
                MyClass.staticvar += 1
        self.endfn(self.i, res)
        return res

    def run(self) -> None:
        self.res = self.huge(self.nb)

def display(i, nb):
    print(f"Thread {i}={nb}")

def end(i, nb):
    print(f"Final Result {i}={nb}")

thread1 = MyClass(1, 50, display, end)
thread2 = MyClass(2, 100, display, end)
thread1.start()
thread2.start()

print(thread1.res)
print(thread2.res)


