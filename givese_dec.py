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
    return render_template("my-form.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if text is None:
        return send_file('none.png')
    else:
        general_dict()
        # return send_file('pict/test.jpg')
        return send_file('foo_new.png')


def general_dict():
    # tworzymy słownik z pixelami dla printable
    pixels_string_printable = {}
    for letter in string.printable:
        if len(pixels_string_printable) == 0:
            pixels_string_printable[letter] = (int(255), int(255), int(255))
        else:
            pixels_string_printable[letter] = (int(len(pixels_string_printable)*2), int(len(pixels_string_printable)*1), int(len(pixels_string_printable)*2))
    # print pixels_string_printable
    open_file(pixels_string_printable)


def open_file(pixels_string_printable):

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
            # if pixels[x, y] == (78, 39, 78):
            #     print dupa
            if last != pixels[x, y]:
                if pixels[x, y] != (255, 255, 255):
                    RGB = photo.getpixel((x, y))
                    R, G, B = RGB
                    image_pixels.append((R, G, B))
            last = pixels[x, y]

    # print image_pixels

    # porownujemy pixele z pliku z printable i tworzymy wynik
    last = None
    image_letter = []
    for pix in image_pixels:
        if pix == (1, 1, 1):
            image_letter.append('?')
        else:
            for letter, pix2 in pixels_string_printable.items():
                if pix == pix2:
                    # zapisujemy tylko nowe pixele
                    if letter != last:
                        image_letter.append(letter)
                    last = letter

    print_sentence = ''.join(image_letter)
    print print_sentence

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=804)
    general_dict()

