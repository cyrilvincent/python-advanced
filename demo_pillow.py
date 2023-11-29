#pip install Pillow

from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(float)
print(array.shape)

print(f"Luminance: {np.mean(array)}")
print(f"Contraste: {np.std(array)}")

nb = np.mean(array, axis=2)
nb = np.clip(nb - 50,0,255)

green = array[10:-10,100:-100,1]
print(green.shape)

dest = Image.fromarray(nb.astype(np.uint8)).convert("RGB")
dest.save("data/out.jpg")
dest.show()

#Reprise 13h45