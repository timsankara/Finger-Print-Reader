from PIL import Image
import sys

im = sys.argv[1]
im2 = Image.open(f"{im}")
im2.save( f"./database/{im}.tiff")