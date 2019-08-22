import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from magicpen.fonts import fonts_map


def get_percent(image, option=False):
    height, width = image.shape
    image = image > 0
    white = np.sum(image)
    size = height * width
    if option:
        return (size - white) / white
    else:
        return (size - white) / size


def get_gray_image(char, font, size):
    image = Image.new('L', (size, size), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font, size)
    draw.text((0, 0), char, 0, font)
    return image


def get_chars(path):
    _chars = list()
    with open(path) as f:
        for _char in f:
            _char = u'{}'.format(_char)
            _chars.append(_char)
    return _chars


def PIL2CV(image, rgb=True):
    image = np.asarray(image)
    if rgb:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image


def get_font_name(font):
    return fonts_map[font]


def get_fonts_names(fonts):
    names = []
    for font in fonts:
        names.append(get_font_name(font))
    return names
