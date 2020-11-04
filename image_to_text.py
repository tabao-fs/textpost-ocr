from PIL import Image
import pyocr.builders

from check_available import get_available_tool, get_available_language


tool = get_available_tool()
lang = get_available_language(tool)

txt = tool.image_to_string(
    Image.open('data/1.jpg'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
print(txt)
