from PIL import Image
import numpy as np
# pip install Pillow

class ImageTreatment :

    def __init__(self):
        self.cube = None
        self.mean = None
        self.std = None
        self.fnorm = lambda x: np.clip(((x - self.mean) / self.std) * 64 + 128, 0, 255)

    @property
    def red(self):
        return self.cube[:,:,0]

    def compute_stats(self):
        self.mean = np.mean(self.cube)
        self.std = np.std(self.cube)

    def load(self, uri):
        im = Image.open(uri)
        self.cube = np.asarray(im).astype(float)
        self.compute_stats()

    def save(self, tensor, uri):
        im = Image.fromarray(tensor.astype(np.uint8)).convert("RGB")
        im.save(uri)

    def crop(self, row, column):
        self.cube = self.cube[row // 2 : -row // 2, column // 2 : -column // 2]

    def to_gray(self):
        return np.mean(self.cube, axis=2)

    def normalize(self):
        self.cube = self.fnorm(self.cube)

if __name__ == '__main__':
    it = ImageTreatment()
    it.load("data/ski.jpg")
    it.crop(100,100)
    it.normalize()
    gray = it.to_gray()
    it.save(it.cube, "data/ski_modified.jpg")




# Clipper, Crop 10 px autour de l'image
# Transformer les 3 canaux de couleur en N/B
# Autocorriger la luminosité fnorm ((px - moy) / std)*64+128
# Charger 3 images et les additionner
