# coding=utf-8
from __future__ import division
import argparse
import string
from PIL import Image
import glob, os
import os.path


def general_dict(text):
    # tworzymy słownik z pixelami dla printable
    s1 = {}
    for letter in string.printable:
        if len(s1) == 0:
            s1[letter] = (int(255/1), int(255/1), int(255/1))
        else:
            s1[letter] = (int(255 / len(s1)*3), int(255 / len(s1))*6, int(255 / len(s1)*9))

    # przypisujemy pixele dla podanego wyrażenia
    s2 = []
    for c in text:
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
    char = 0
    for value in s2:
        i = Image.new(mode='RGB', size=(20, 20), color=value[1])
        # czy plik istnieje?
        if not os.path.isfile(('pict/' + str(value) + '_' + str(char) + '.png')):
             i.save('pict/' + str(value) + '_' + str(char) + '.png')
        else:
            char += 1
            i.save('pict/' + str(value) + '_' + str(char) + '.png')


    create_one_file()
    

# tworzymy jeden plik wyjściowy z podanimy w zdaniu pixelami
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
    #     args.text = raw_input('Please input path and name of the file > ')

    if not args.text:
        args.text = 'Ta epopeja narodowa z elementami gawędy szlacheckiej powstała w latach 1832–1834 w Paryżu. Składa się z dwunastu ksiąg pisanych wierszem, trzynastozgłoskowym aleksandrynem polskim. Czas akcji: pięć dni z roku 1811 i dwa dni z roku 1812.'

    general_dict(args.text)