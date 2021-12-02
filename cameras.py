from abc import ABCMeta, abstractmethod
from typing import List

class ICameraAcquire(metaclass=ABCMeta):

    @abstractmethod
    def acquire(self): ...

    @abstractmethod
    def calibrate(self): ...

class CameraAcquire(ICameraAcquire, metaclass=ABCMeta):

    def calibrate(self):
        print("Default calibrate")



class SerialAcquire(CameraAcquire):

    def acquire(self):
        print("Serial acquire")

    def calibrate(self):
        print("Serial Calibrate")

class USBAcquire(CameraAcquire):

    def acquire(self):
        print("USB acquire")

class CameraService:

    def __init__(self, cameras):
        self.cameras: List[ICameraAcquire] = cameras

    def acquire_all_cameras(self):
        for camera in self.cameras:
            camera.acquire()


if __name__ == '__main__':
    l = [SerialAcquire(), USBAcquire()]
    service = CameraService(l)
    service.acquire_all_cameras()
