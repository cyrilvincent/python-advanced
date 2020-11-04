import threading
import time

class  MyThread(threading.Thread):

    def __init__(self, id, sleep):
        super().__init__()
        self.id = id
        self.sleep = sleep

    def run(self) -> None:
        for i in range(20):
            print(f"Thread {self.id}: {i}")
            time.sleep(self.sleep)

thread1 = MyThread(1,0.5)
thread2 = MyThread(2,1)
thread3 = MyThread(3,1.5)

thread1.start()
thread2.start()
thread3.start()