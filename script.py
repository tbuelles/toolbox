import os
from wand.image import Image
import json


with open('path.json', 'r') as f:
    PATH = json.load(f)
    src_dir = PATH.get('src_dir')
    dst_dir = PATH.get('dst_dir')

for count, file in enumerate(os.listdir(src_dir)):
    src = src_dir + file
    dst = dst_dir + str(count) + '.jpg'
    if src == '.DS_Store':
        continue
    with Image(filename=src) as img:
        img.format = 'jpg'
        img.save(filename=dst)
