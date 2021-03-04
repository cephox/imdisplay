#!/bin/python

import os
from argparse import ArgumentParser

from image import transform_to_ascii, get_image, grayify_image, resize_image


def parse():
    width_default = os.get_terminal_size()[0]

    parser = ArgumentParser(description="A tool to display an image in your terminal")
    parser.add_argument("image", metavar="path", type=str, help="The path for the image to display")
    parser.add_argument("--width", type=int, help="the width for the image to be displayed", default=width_default)
    parser.add_argument("--gray", "--grey", action="store_const", const=grayify_image, default=nop, dest="gray",
                        help="prints the image in grayscale")
    return parser.parse_args()


def nop(any):
    return any


def main():
    args = parse()
    print(transform_to_ascii(args.gray(resize_image(get_image(args.image), args.width))))


if __name__ == '__main__':
    main()
