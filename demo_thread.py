import threading
import time

class MyThread(threading.Thread):

    def __init__(self, num, sleep, nb):
        super().__init__()
        self.num = num
        self.sleep = sleep
        self.nb = nb
        self.i = 1

    def run(self):
        for j in range(self.nb):
            print(f"Thread {self.num} => {self.i}")
            self.i *= 2
            time.sleep(self.sleep)


if __name__ == '__main__':
    th1 = MyThread(1, 0.1, 100)
    th2 = MyThread(2, 0.05, 80)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(th1.i)
    print(th2.i)

