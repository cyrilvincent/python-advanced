import numpy as np
import matplotlib.pyplot as plt
import threading
import time

class MesureThread(threading.Thread):

    def __init__(self, step, nb_period, fn):
        super().__init__()
        self.step = step
        self.nb_period = nb_period
        self.fn = fn

    def run(self):
        for i in np.arange(0, self.nb_period*2*np.pi, self.step):
            self.fn(i, np.sin(i))
            time.sleep(self.step * 10)

results = []

def display(step, result, first=False):
    results.append(result)
    print(results)
    plt.scatter(np.arange(len(results)), results)
    plt.draw()


if __name__ == '__main__':
    thread1 = MesureThread(0.1, 0.1, display)
    plt.ion()
    display(0,0, True)
    thread1.start()


