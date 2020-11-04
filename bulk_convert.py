import glob

from check_available import (
    get_available_tool, get_available_language,
    get_text_builder
)

EXTENSIONS = ('*.jpg', '*.jpeg', '*.png')


def get_images(path):
    images = []
    for extension in EXTENSIONS:
        images.extend(glob.glob(path + extension))
    return images


if __name__ == '__main__':
    '''
    Bulk convert images to texts
    '''
    tool = get_available_tool()
    lang = get_available_language(tool)
    builder = get_text_builder()
    path = 'data/'
    images = get_images(path)
    print(images)
