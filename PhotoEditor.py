from PIL import Image
im = Image.open("shreks.jpg")
print(im.format, im.size, im.mode)
im.show()

import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)

box = (100, 100, 400, 400)
region = im.crop(box)

region = region.transpose(Image.Transpose.ROTATE_180)
im.paste(region, box)

