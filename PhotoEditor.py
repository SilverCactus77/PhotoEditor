from PIL import Image
print("pick a photo (Shrek, Ronaldo):")

x = input()
if x == "Shrek":
    Image = Image.open("Shreks.jpg")
    print(Image.format, Image.size, Image.mode)
    Image.show()

y = input()
if y == "Ronaldo":
    Image2 = Image.open("Ronaldo.jpeg")
    print(Image2.format, Image2.size, Image2.mode)
    Image2.show()