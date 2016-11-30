# coding=utf-8
from __future__ import division
import string
from PIL import Image, ImageDraw
import glob, os, random, os.path
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack, send_file


app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("enter_sentence.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if text is None:
        return send_file('none.png')
    else:
        g2_dict(text)
        return send_file('foo_new.png')


@app.route('/text', methods=['GET'])
def get_data():
    x = open_file()
    return x, 200, {'Content-Type': 'text/html; charset=utf-8'}


def g2_dict(text):
    # tworzymy słownik z pixelami dla printable
    s1 = {}
    for letter in string.printable:
        if len(s1) == 0:
            s1[letter] = (int(255), int(255), int(255))
        else:
            s1[letter] = (int(len(s1)*2), int(len(s1)*1), int(len(s1)*2))

    new_file(get_pixels_for_sentence(text, s1))


def get_pixels_for_sentence(text, s1):
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

    return s2


def new_file(s2):
    path = r'p/'
    random_filename = random.choice([x for x in os.listdir(path)])
    i = Image.open('p/' + random_filename)

    photo = i.convert('RGB')

    pixels = photo.load()
    width, height = photo.size

    last = None
    last2 = None
    last3 = 0
    new_im = Image.new('RGB', (width, height), (255, 255, 255))

    for x in range(width):
        for y in range(height):
            if pixels[x, y] != (255, 255, 255):
                # dla każdego powtarzającego sie RGB w tej samej linii przypisujemy nowe RGB w nowym pliku
                if last == pixels[x, y]:
                    if last2 == [x, y][0]:
                        # wstawianie pixeli z podanego przez użytkownika zdania
                        new_im.putpixel([x, y], s2[last3][1])
                        # przypisujemy pixele tak długo, dopóki nie wyczerpiemy podanego zdania
                    elif last3 != len(s2)-1:
                        last3 += 1
                    last2 = [x, y][0]
                last = pixels[x, y]
    new_im.save("foo_new.png")


def g1_dict():
    # tworzymy słownik z pixelami dla printable
    pixels_string_printable = {}
    for letter in string.printable:
        if len(pixels_string_printable) == 0:
            pixels_string_printable[letter] = (int(255), int(255), int(255))
        else:
            pixels_string_printable[letter] = (int(len(pixels_string_printable)*2), int(len(pixels_string_printable)*1), int(len(pixels_string_printable)*2))
    # print pixels_string_printable
    return pixels_string_printable


def open_file():
    photo = Image.open('foo_new.png')
    photo = photo.convert('RGB')
    pixels = photo.load()
    width = photo.size[0]
    height = photo.size[1]

    # czytamy pixele z otwartego pliku
    last = None
    image_pixels = []
    for x in range(0, width):
        for y in range(0, height):
            if last != pixels[x, y]:
                if pixels[x, y] != (255, 255, 255):
                    RGB = photo.getpixel((x, y))
                    R, G, B = RGB
                    image_pixels.append((R, G, B))
            last = pixels[x, y]

    # porownujemy pixele z pliku z printable i tworzymy wynik
    last = None
    image_letter = []
    for pix in image_pixels:
        if pix == (1, 1, 1):
            image_letter.append('?')
        else:
            pixels_string_printable = g1_dict()
            for letter, pix2 in pixels_string_printable.items():
                if pix == pix2:
                    # zapisujemy tylko nowe pixele
                    if letter != last:
                        image_letter.append(letter)
                    last = letter

    sentence = ''.join(image_letter)
    print sentence
    return sentence


if __name__ == '__main__':
    # text = 'Dawwwwwid'
    app.run(debug=True, host='0.0.0.0', port=804)
    # g2_dict(text)
