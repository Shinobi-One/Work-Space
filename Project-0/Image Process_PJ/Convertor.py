import sys

import os


from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]


if not  os.path.exists(output_folder):
	os.makedirs(output_folder) # python convertor.py \poco \new  cmd  رد

for filename in os.listdir(image_folder):
	pic = Image.open(f"{image_folder}{filename}")
	clean_pic = os.path.splitext(filename)[0]
	pic.save(f"{output_folder}{clean_pic}.png")
