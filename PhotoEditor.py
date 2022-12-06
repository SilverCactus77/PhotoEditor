from PIL import Image
from PIL import ImageEnhance
print("pick a photo (Shrek, Ronaldo):")

x = input()
if x == "Shrek":
    Image = Image.open("Shreks.jpg")
    print(Image.format, Image.size, Image.mode)
    Image.show()

if x == "Ronaldo":
    Image = Image.open("Ronaldo.jpg")
    print(Image.format, Image.size, Image.mode)
    Image.show()

print("pick a filter (Cursed, Enhance, Squeeze)")

if x == "Shrek":
    y = input()
    if y == "Cursed":
        enh = ImageEnhance.Contrast(Image)
        enh.enhance(4.5).show("50% more contrast")

if x == "Ronaldo":
    y = input()
    if y == "Cursed":
        enh = ImageEnhance.Contrast(Image)
        enh.enhance(4.5).show("50% more contrast")

if x == "Shrek":
    y = input()
    if y == "Enhance":
        enhancer = ImageEnhance.Sharpness(Image)
        enhancer

