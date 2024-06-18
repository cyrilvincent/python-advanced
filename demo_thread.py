import threading
import time

class MyThread(threading.Thread):

    def __init__(self, num: int, pause:float, fn, progress_fn):
        super().__init__()
        self.num = num
        self.pause = pause
        self.fn = fn
        self.progress_fn = progress_fn
        self.res = 1

    def run(self):
        for i in range(100):
            self.res *= 2
            # print(f"Message de la thread {self.num}: {self.res}")
            time.sleep(self.pause)
            self.progress_fn(self.num, i / 100)
        self.fn(self.num, self.res)

def display_final(num: int, result: int):
    print(f"Thread {num} final result {result}")

def progress(num: int, completion: float):
    print(f"Thread {num} progress {completion*100:.1f}%")

if __name__ == '__main__':
    thread1 = MyThread(1, 0.15, display_final, progress)
    thread2 = MyThread(2,0.1, display_final, progress)
    thread3 = MyThread(3, 0.2, display_final, progress)
    thread1.start()
    thread2.start()
    thread3.start()
    # thread1.join()
    # thread2.join()
    # print(f"Result {thread1.res}")
    # print(f"Result {thread2.res}")