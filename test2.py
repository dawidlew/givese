# coding=utf-8
from PIL import Image
i = Image.open("g1.png")

photo = i.convert('RGB')

pixels = photo.load()
width, height = photo.size


s1 = []
last = None
last2 = None
for x in range(width):
    for y in range(height):
        # dla każdego powtarzającego sie RGB w tej samej linii przypisujemy nowe RGB
        if last == pixels[x, y]:
            if last2 == [x, y][0]:
                pixels[x, y] = (0, 0, 0)
                s1.append([(247, 255, 0), [x, y]])
            last2 = [x, y][0]
        last = pixels[x, y]

        i.save("foo_new.png")



# x = 0
# for p in all_pixels:
#     print all_pixels[x]
#     x += 1
