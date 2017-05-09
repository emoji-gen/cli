# -*- coding: utf-8 -*-

import sys
import argparse

from String2emoji import String2emoji

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('messages', type=str, nargs='+', help='emoji message')
    parser.add_argument('-f', '--font', type=str, nargs='?', help='set font (default=NotoSansCJKjp-hinted/NotoSansMonoCJKjp-Bold.otf)')
    parser.add_argument('-o', '--out', type=str, nargs='?', help='output image file (default=test.png)')
    parser.add_argument('-c', '--color',type=str, nargs='?',help='set font color(default=000000')
    parser.set_defaults(font='NotoSansCJKjp-hinted/NotoSansMonoCJKjp-Bold.otf', out='test2.png',color='000000')

    args = parser.parse_args()

    argv = args.messages
    argc = len(argv)

    fontFile = args.font
    imageFile = args.out
    r = int(args.color[0] +args.color[1],16)
    g = int(args.color[2] +args.color[3],16)
    b = int(args.color[4] +args.color[5],16)

    text = []
    for num in range(0, argc):
        text.append(argv[num])
    emoji = String2emoji(text, fontFile,(r,g,b))

    img = emoji.getEmoji()

    img.save(imageFile)


if __name__ == '__main__':
    main()
