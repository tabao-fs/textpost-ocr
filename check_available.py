from PIL import Image
import sys

import pyocr
import pyocr.builders


def get_available_tool():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    return tools[0]

tool = get_available_tool()
print("Will use tool: '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang: '%s'" % (lang))
