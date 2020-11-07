import sys
from PIL import Image
import codecs

from check_available import (
    get_available_tool, get_available_language,
    get_text_builder
)


def image_to_string(tool, lang, builder, filename):
    return tool.image_to_string(
        Image.open(filename),
        lang=lang,
        builder=builder
    )


def write_text_file(filename, text, builder):
    with codecs.open(filename, 'w', encoding='utf-8') as file_descriptor:
        builder.write_file(file_descriptor, text)


def convert_image(filename):
    tool = get_available_tool()
    lang = get_available_language(tool)
    builder = get_text_builder()
    text = image_to_string(tool, lang, builder, filename)

    return text

if __name__ == '__main__':
    '''
    Convert image to text
    '''
    if len(sys.argv) <= 1:
        print("Image file was not provided. Please try again.")
    else:
        text = convert_image(sys.argv[1])
        print(text)
