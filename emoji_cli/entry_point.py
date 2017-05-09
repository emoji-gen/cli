# -*- coding: utf-8 -*-

import sys
import argparse

from emoji_lib import String2Emoji

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('messages', type=str, nargs='+', help='emoji message')
    parser.add_argument('-f', '--font', type=str, nargs='?', \
        help='set font (default=NotoSansCJKjp-hinted/NotoSansMonoCJKjp-Bold.otf)')
    parser.add_argument('-o', '--out', type=str, nargs='?', \
        help='output image file (default=out.png)')
    parser.add_argument('-c', '--color', type=str, nargs='?', \
        help='set font color(default=000000')
    parser.set_defaults( \
        font='NotoSansCJKjp-hinted/NotoSansMonoCJKjp-Bold.otf', \
        out='out.png', \
        color='000000')

    args = parser.parse_args()

    argv = args.messages
    argc = len(argv)

    font_file = args.font
    image_file = args.out
    r_color = int(args.color[0]+args.color[1], 16)
    g_color = int(args.color[2]+args.color[3], 16)
    b_color = int(args.color[4]+args.color[5], 16)

    text = []
    for num in range(0, argc):
        text.append(argv[num])
    emoji = String2Emoji(text, font_file, (r_color, g_color, b_color))

    img = emoji.getEmoji()

    img.save(image_file)


if __name__ == '__main__':
    main()
