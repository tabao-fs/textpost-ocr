import glob
import os

from check_available import (
    get_available_tool, get_available_language,
    get_text_builder
)
from image_to_text import image_to_string, write_text_file


EXTENSIONS = ('*.jpg', '*.jpeg', '*.png')
INPUT = 'data/'
OUTPUT = 'output/'
TXT_EXTENSION = '.txt'


def get_images(path):
    images = []
    for extension in EXTENSIONS:
        images.extend(glob.glob(path + extension))
    return images


def bulk_convert_images(images, tool, lang, builder):
    for image in images:
        filename = os.path.basename(image)
        txt = image_to_string(tool, lang, builder, image)
        write_text_file(OUTPUT + filename + TXT_EXTENSION, txt, builder)


if __name__ == '__main__':
    '''
    Bulk convert images to texts
    '''
    tool = get_available_tool()
    lang = get_available_language(tool)
    builder = get_text_builder()

    images = get_images(INPUT)
    bulk_convert_images(images, tool, lang, builder)
