import unittest
import cameras

class MyTests(unittest.TestCase):

    def test_camera_acquire(self):
        acquire = cameras.SerialAcquire()
        acquire.acquire()
        acquire2 = cameras.USBAcquire()
        acquire2.acquire()
        # cameras.CameraAcquire()