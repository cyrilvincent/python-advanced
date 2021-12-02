import threading
import time

class MyThread(threading.Thread):

    def __init__(self, num: int, sleep: float, endFn, progressFn):
        super().__init__()
        self.num = num
        self.sleep = sleep
        self.result = 0
        self.endFn = endFn
        self.progressFn = progressFn

    def huge_compute(self, nb):
        res = 1
        for i in range(nb):
            res *= 2
            # print(f"Thread {self.num} => {res}")
            time.sleep(self.sleep)
            if i % 10 == 0:
                self.progressFn(self.num, i / nb)
        return res

    def run(self) -> None:
        self.result = self.huge_compute(100)
        self.endFn(self.num, self.result)

class MainService:
    def display_result(self, num: int, result: int):
        print(f"Result from thread {num} = {result}")

    def display_progress(self, num: int, progress: int):
        print(f"Progress from thread {num} = {progress * 100:0.1f}%")

if __name__ == '__main__':
    service = MainService()
    t1 = MyThread(1, 0.1, service.display_result, service.display_progress)
    t1.start()
    t2 = MyThread(2, 0.05, service.display_result, service.display_progress)
    t2.start()
    print(t1.result, t2.result)