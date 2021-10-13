import threading
import time

class HugeCompute(threading.Thread):

    def __init__(self, num, sleep, nb_iter, end_fn, progress_fn):
        super().__init__()
        self.num = num
        self.sleep = sleep
        self.nb_iter = nb_iter
        self.result = 0
        self.end_fn = end_fn
        self.progress_fn = progress_fn

    def run(self) -> None:
        for i in range(self.nb_iter):
            # print(f"Thread {self.num}: {i}")
            time.sleep(self.sleep)
            self.result += 1
            if i % 10 == 0:
                self.progress_fn(self, i / 100)
        self.end_fn(self)


if __name__ == '__main__':

    def my_end_fn(thread):
        print(f"Result {thread.num}: {thread.result}")

    def my_progress_fn(thread, completion):
        print(f"Progress {thread.num}: {thread.result} {completion*100:.2f}%")

    hc1 = HugeCompute(1, 0.1, 100, my_end_fn, my_progress_fn)
    hc2 = HugeCompute(2, 0.15, 50, my_end_fn, my_progress_fn)
    hc3 = HugeCompute(3, 0.33, 10, my_end_fn, my_progress_fn)
    hc1.start()
    hc2.start()
    hc3.start()
    # hc1.join()
    # hc2.join()
    # hc3.join()

