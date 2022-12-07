from PIL import Image, ImageOps
from PIL import ImageEnhance
# user picks photo
print("pick a photo (Shrek, Ronaldo):")

# user inputs which photo they would like to see
x = input()
if x == "Shrek":
    Image = Image.open("Shreks.jpg")
    print(Image.format, Image.size, Image.mode)
    Image.show()

if x == "Ronaldo":
    Image = Image.open("Ronaldo.jpg")
    print(Image.format, Image.size, Image.mode)
    Image.show()

# user selects a filter from the options below
print("pick a filter (Cursed, Rotate, Grey)")

# applies the filter chosen by the user
if x == "Shrek":
    y = input()
    if y == "Cursed":
        enh = ImageEnhance.Contrast(Image)
        enh.enhance(4.5).show("Way more contrast")
    if y == "Rotate":
        im_rotate = Image.rotate(90)
        im_rotate.show()
    if y == "Grey":
        gray_image = ImageOps.grayscale(Image)
        gray_image.show()

if x == "Ronaldo":
    y = input()
    if y == "Cursed":
        enh = ImageEnhance.Contrast(Image)
        enh.enhance(4.5).show("Way more contrast")
    if y == "Rotate":
        im_rotate = Image.rotate(90)
        im_rotate.show()
    if y == "Grey":
        gray_image = ImageOps.grayscale(Image)
        gray_image.show()


