from PIL import Image
import pyocr.builders

from check_available import get_available_tool, get_available_language


def image_to_string(tool, lang, builder, filename):
    return tool.image_to_string(
        Image.open(filename),
        lang=lang,
        builder=builder
    )


if __name__ == '__main__':
    '''
    Convert image to text
    '''
    tool = get_available_tool()
    lang = get_available_language(tool)
    builder = pyocr.builders.TextBuilder()
    filename = 'data/1.jpg'

    txt = image_to_string(tool, lang, builder, filename)
    print(txt)
