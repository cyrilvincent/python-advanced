from PIL import Image
import numpy as np

class ImageService:

    def __init__(self, path: str):
        im = Image.open(path)
        self.array = np.asarray(im).astype(float)

    def luminance(self):
        return np.mean(self.array)

    def luminance_by_chanel(self, chanel):
        return np.mean(self.array[:,:,chanel])

    def contrast(self):
        return np.std(self.array)

    def contrast_by_chanel(self, chanel):
        return np.std(self.array[:,:,chanel])

    def dynamic(self):
        return np.max(self.array) - np.min(self.array)

    def crop(self, east, west, north, south):
        self.array = self.array[north:-south, east:-west]

    def save(self, path: str):
        dest = Image.fromarray(self.array.astype(np.uint8)).convert("RGB")
        dest.save(path)

    def display(self):
        dest = Image.fromarray(self.array.astype(np.uint8)).convert("RGB")
        dest.show()

    def change_luminance(self, delta):
        self.array = np.clip(self.array + delta, 0, 255)

    def change_contrast(self, ratio):
        self.array = np.clip((self.array - self.luminance()) * ratio + self.luminance() , 0, 255)


if __name__ == '__main__':
    service = ImageService("data/ski.jpg")
    # service.display()
    print(service.luminance(), service.luminance_by_chanel(0))
    print(service.contrast(), service.contrast_by_chanel(0))
    print(service.dynamic())
    #service.crop(100,200,50,50)
    #service.display()
    service.change_luminance(127.5 - service.luminance())
    service.change_contrast(1.1)
    service.display()


