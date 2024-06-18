import threading
import time

class MyThread(threading.Thread):

    def __init__(self, num: int, pause:float):
        super().__init__()
        self.num = num
        self.pause = pause
        self.res = 1

    def run(self):
        for i in range(100):
            self.res *= 2
            print(f"Message de la thread {self.num}: {self.res}")
            time.sleep(self.pause)

if __name__ == '__main__':
    thread1 = MyThread(1, 0.15)
    thread2 = MyThread(2,0.1)
    thread1.start()
    thread2.start()