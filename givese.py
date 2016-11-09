# coding=utf-8
from __future__ import division
import argparse
import string
from PIL import Image
import glob, os
import os.path
import time



def general_dict(text):
    # tworzymy słownik z pixelami dla printable
    s1 = {}
    for letter in string.printable:
        if len(s1) == 0:
            s1[letter] = (int(255), int(255), int(255))
        else:
            s1[letter] = (int(255 / (len(s1)/20)), int(255 / (len(s1))*5), int(255 / (len(s1))))

    # przypisujemy pixele dla podanego zdania
    s2 = []
    y = 0
    for c in text:
        if c not in string.printable:
            # usuwanie podójnego wiersza dla dziwnych znakow
            if y == 0:
                s2.append(['?', (1, 1, 1)])
                y = 1
            else:
                y = 0
        else:
            for k, p in s1.items():
                if k == c:
                    s2.append([c, p])

    for x in s2:
        print x

    # usuwamy pliki z katalogu lub tworzymy katalog
    if os.path.isdir('pict/'):
        filelist = glob.glob('pict/*.*')
        for f in filelist:
            os.remove(f)
    else:
        os.mkdir('pict')

    # zapełniamy katalog plikami
    char = 100 # dla poprawnego sortowania plików jak jest ich więcej niz 100, a prawie zawsze jest
    for value in s2:
        i = Image.new(mode='RGB', size=(20, 20), color=value[1])

        i.save('pict/' + str(char) + '.png')

        char += 1

    create_one_file()


# tworzymy jeden plik wyjściowy ze zmapowanymi pixelami
def create_one_file():

    images = map(Image.open, glob.glob('pict/*.png'))
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0

    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('pict/test.jpg')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str,
                        help="Text to convert",
                        required=False)
    args = parser.parse_args()

    # if not args.text:
    #     args.text = raw_input('Please input sentences to change > ')

    if not args.text:
        args.text = 'Pingwin urodził dziecko'

    general_dict(args.text)