import glob
import os

from check_available import (
    get_available_tool, get_available_language,
    get_text_builder
)
from image_to_text import image_to_string, write_text_file


EXTENSIONS = ('*.jpg', '*.jpeg', '*.png')
OUTPUT = 'output/'


def get_images(path):
    images = []
    for extension in EXTENSIONS:
        images.extend(glob.glob(path + extension))
    return images


def bulk_convert_images(images, tool, lang, builder):
    for image in images:
        filename = os.path.basename(image)
        txt = image_to_string(tool, lang, builder, image)
        write_text_file(OUTPUT + filename + '.txt', txt, builder)


if __name__ == '__main__':
    '''
    Bulk convert images to texts
    '''
    tool = get_available_tool()
    lang = get_available_language(tool)
    builder = get_text_builder()
    path = 'data/'

    images = get_images(path)
    bulk_convert_images(images, tool, lang, builder)
