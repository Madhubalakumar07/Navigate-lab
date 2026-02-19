import numpy as np
from PIL import Image
image  = Image.open("D:/Madhu/download.png")
img_array = np.array(image)
brightened_image = img_array + 10
brightened_image = np.clip(brightened_image, 0, 255)
brightened_image = brightened_image.astype(np.uint8)
brightened_image_pil = Image.fromarray(brightened_image)
brightened_image_pil.show()