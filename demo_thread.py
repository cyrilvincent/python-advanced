import time
import threading

class MaClasse(threading.Thread):

    def __init__(self, id: int, nb: int, sleep: float):
        super().__init__()
        self.id = id
        self.nb = nb
        self.sleep = sleep
        self.result = 1

    def huge_computing(self):
        for i in range(self.nb):
            print(f"Thread {self.id}={self.result}")
            self.result *= 2
            time.sleep(self.sleep)

    def run(self):
        self.huge_computing()

c1 = MaClasse(1, 100, 0.1)
c2 = MaClasse(2, 50, 0.1)
c3 = MaClasse(3, 20, 0.6)
l = [c1, c2, c3]
for t in l:
    t.start()