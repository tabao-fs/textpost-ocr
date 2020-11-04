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


if __name__ == '__main__':
    '''
    Convert image to text
    '''
    tool = get_available_tool()
    lang = get_available_language(tool)
    builder = get_text_builder()
    filename = 'data/1.jpg'

    txt = image_to_string(tool, lang, builder, filename)

    filename = 'output/1.txt'
    write_text_file(filename, txt, builder)

    print(txt)
