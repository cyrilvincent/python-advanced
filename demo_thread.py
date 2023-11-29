import time
import threading

class MyThread(threading.Thread):

    def __init__(self, num, sleep, slot):
        super().__init__()
        self.num = num
        self.sleep = sleep
        self.slot = slot

    def run(self):
        i = 1
        for j in range(100):
            print(f"Thread {self.num} => {i}")
            time.sleep(self.sleep)
            i = i * 2
        #print(f"Result {self.num} => {i}")
        self.slot(i, self.num)

def result_slot(result, num):
    print(f"Result {result} from thread {num}")

if __name__ == '__main__':
    thread1 = MyThread(1,0.1, result_slot)
    thread2 = MyThread(2,0.05, result_slot)
    thread1.start()
    thread2.start()




