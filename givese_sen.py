# coding=utf-8
from __future__ import division
import string
from PIL import Image
import glob, os
import os.path
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack, send_file
import random

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
        general_dict(text)
        return send_file('pict/test.jpg')


def general_dict(text):

    # tworzymy słownik z pixelami dla printable
    s1 = {}
    for letter in string.printable:
        if len(s1) == 0:
            s1[letter] = (int(255), int(255), int(255))
        else:
            s1[letter] = (int(255 / (len(s1)/20)), int(255 / (len(s1))*5), int(255 / (len(s1))))

    clear_dir()
    make_dir_full(get_pixels_for_sentence(text, s1))
    create_one_file()


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


def clear_dir():
    # usuwamy pliki z katalogu lub tworzymy katalog
    if os.path.isdir('pict/'):
        filelist = glob.glob('pict/*.*')
        for f in filelist:
            os.remove(f)
    else:
        os.mkdir('pict')


def make_dir_full(s2):
    # zapełniamy katalog plikami
    char = 100 # dla poprawnego sortowania plików jak jest ich więcej niz 100, a prawie zawsze jest
    for value in s2:
        i = Image.new(mode='RGB', size=(20, 20), color=value[1])
        i.save('pict/' + str(char) + '.png')
        char += 1


# tworzymy jeden plik wyjściowy ze zmapowanymi pixelami
def create_one_file():
    images = map(Image.open, glob.glob('pict/*.png'))
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    total_height = sum(heights)
    new_im = Image.new('RGB', (total_width, total_height), (255, 255, 255))
    x = 0
    y = 0
    for im in images:
        new_im.paste(im, (x, y))
        x += im.size[0]
        y = int(random.random() * 400)

    new_im.save('pict/test.jpg')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=803)