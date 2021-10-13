from PIL import Image
import numpy as np
# pip install Pillow

im = Image.open("data/ski.jpg")
cube = np.asarray(im).astype(float)
print(cube.shape)

red = cube[:,:,0]
print(np.min(red), np.max(red), np.mean(red), np.std(red))

red = red.T

np.clip(127,0,255)

im = Image.fromarray(red.astype(np.uint8)).convert("RGB")
im.save("data/ski_modified.jpg")

# Clipper, Crop 10 px autour de l'image
# Transformer les 3 canaux de couleur en N/B
# Autocorriger la luminosité
# Charger 3 images et les additionner fnorm ((px - moy) / std)*64+128
