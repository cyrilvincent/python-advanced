from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(float)
print(array.shape)

lum = np.mean(array)
print(lum, np.mean(array[:,:,0]), np.mean(array[:,:,1]), np.mean(array[:,:,2]))

red = array[:,:,0]
print(red.shape)

contrast = np.std(array)
print(contrast)

lum_modified = np.clip(array - 47, 0, 255)

crop = red[100:-100,100:-100]

dest = Image.fromarray(lum_modified.astype(np.uint8)).convert("RGB")
dest.save("data/out.jpg")
dest.show()

# TP
# Porter celà en OO
# lum, contrast, lum_by_chanel(0), contrast_by_chanel(0), crop, save, display, change_lum, change_contrast


