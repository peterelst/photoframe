#!/usr/bin/env python

import argparse
from PIL import Image
from inky import InkyWHAT
import requests

# Keyword for random photo to search
keyword = 'cat'
image_url = 'https://source.unsplash.com/400x300/?{0}'.format(keyword)
# Filename for downloaded image
img_file = 'photo.jpg'


def main():
    # Initialize InkyWHAT display
    inky_display = InkyWHAT('black')

    # Download image and save locally
    img_data = requests.get(image_url).content
    with open(img_file, 'wb') as handler:
        handler.write(img_data)

    # Open downloaded image
    img = Image.open(img_file)

    # Dither downloaded image
    pal_img = Image.new('P', (1, 1))
    pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)
    img = img.convert('RGB').quantize(palette=pal_img)

    # Display dithered image
    inky_display.set_image(img)
    inky_display.show()


if __name__ == '__main__':
  main()
