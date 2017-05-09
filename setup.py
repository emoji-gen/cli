#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name             = 'emoji_cli',
    version          = '0.1.0',
    description      = 'Ultimate Emoji Generator for CLI',
    license          = 'MIT',
    author           = 'pine, jiuya',
    author_email     = 'pinemz@gmail.com',
    url              = 'http://github.com/emoji-gen/Emoji-CLI',
    keywords         = 'emoji generator',
    packages         = ['emoji_cli', 'emoji_lib'],
    package_data     = {},
    entry_points     = {'console_scripts': ['emoji-gen = emoji_cli:main']},
    install_requires = [
        'Pillow >= 4.1.1',
    ],
)

