from PIL import Image
i = Image.open("g.png")

photo = i.convert('RGB')

pixels = photo.load() # this is not a list, nor is it list()'able
width, height = photo.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        print cpixel
        if cpixel == (0, 0, 0):
            print 'dupa'
        else:
            all_pixels.append(cpixel)

# print all_pixels
