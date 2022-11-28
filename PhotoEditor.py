from PIL import Image
im = Image.open("shreks.jpg")
print(im.format, im.size, im.mode)
im.show()
