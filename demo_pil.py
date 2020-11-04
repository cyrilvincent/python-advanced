from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im)
print(cube.shape)
red = cube[:,:,0]
nb = np.mean(cube, axis = 2)
print(nb.shape)
print(nb)
print(np.min(nb), np.max(nb))
print(f"Luminance: {np.mean(nb)}")
print(f"Contrast:  {np.std(nb)}")

def norm(x, avg, std):
    return (x - avg) / std

nb_norm = norm(nb, np.mean(nb), np.std(nb))
nb_norm = np.clip(nb_norm * 64 + 127.5,0,255)


im = Image.fromarray(nb_norm).convert("RGB")
im.save("data/ski_modified.jpg")

# Masque => laisser passer les points > 127.5 et mettre à 0 les autres
# Masque cosine => laisser passer les cos > 0