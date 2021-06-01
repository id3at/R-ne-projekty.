import os
from PIL import Image

x = 0
for t in os.listdir():
    if "jpg" in str(t):
        new_width  = 400
        
        image = Image.open(t) 
        size = image.size
        new_height = new_width * size[1] / size[0] 
        print(image.size)
        resize_img  = image.resize((new_width, int(new_height)), Image.ANTIALIAS)
        resize_img.save(f"{x}+{t}")
        x += 0


