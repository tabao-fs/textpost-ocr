from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
langs = tool.get_available_languages()
lang = langs[0]

txt = tool.image_to_string(
    Image.open('data/1.jpg'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
print(txt)
