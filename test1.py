# coding=utf-8
from __future__ import division
import string
from PIL import Image, ImageDraw
import glob, os, random, os.path
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack, send_file, Response
import urllib
import json

text = "iVBORw0KGgoAAAANSUhEUgAAAEEAAAAtCAIAAAB+o5EzAAAAzUlEQVR4nO3ZMQqEMBCF4dkl3UI6\nt5lqey/h/a9hLpDCZotYRIIEI+uC+gbeXwhCivkwsckjpSTGcyIyfIYxjtN3unuYpRDDofWue3X9\nuz9pmv9Sr4fWP0+a48powIgGjGjAiAaMaMCIBoxowIgGjGjAiAaMaMCIBoxowIgGjGjAiAaM3N0D\n1FUXWb/cCcEZqqEzaV+CvpfUq3rdv2VEN4hIiCEzWhIDhryR8nOTYcCwnnvzgxgwlANdPkh1QgwY\nWhUG3L+1VT7Z5XV9PGZhfTeMgT/2cwAAAABJRU5ErkJggg==\n"

fh = open("imageToSave.png", "wb")
fh.write(text.decode('base64'))
fh.close()


