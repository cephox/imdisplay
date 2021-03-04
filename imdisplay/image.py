from sys import stderr

from PIL.Image import Image, open
from colr import color


def get_image(path: str) -> Image:
    try:
        return open(path)
    except ValueError:
        stderr.write(path + " is not an image!\n")
        exit(1)
    except TypeError:
        stderr.write(path + " is not an image!\n")
        exit(1)
    except FileNotFoundError:
        stderr.write(path + " is not an image!\n")
        exit(1)


def grayify_image(img: Image) -> Image:
    return img.convert("L")


def resize_image(img: Image, width: int) -> Image:
    current_width, height = img.size
    new_height = int(width / (2 * (current_width / height)))
    return img.resize((width, new_height))


def transform_to_ascii(img: Image) -> str:
    if img.mode == "L":
        return generate_grayscale_ascii(img)
    else:
        return generate_ascii(img)


def generate_grayscale_ascii(img: Image) -> str:
    k = 0
    ret = ""

    for i in img.getdata():
        k += 1
        ret += (l := ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "][::-1])[i % len(l)]
        if k % img.size[0] == 0:
            ret += "\n"

    return ret


def generate_ascii(img: Image) -> str:
    k = 0
    ret = ""

    for i in img.getdata():
        k += 1
        ret += color(" ", fore=(i[0], i[1], i[2]), back=(i[0], i[1], i[2]))
        if k % img.size[0] == 0:
            ret += "\n"

    return ret
