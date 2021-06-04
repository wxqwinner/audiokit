"""
utils.py Utils.

@history
 2021-06-04 wangxq Created.

Copyright (c) 2021~ wangxq.
"""

import os

SUPPORT_FORMATS = ['wav', 'mp3']

def get_format(filename):
    format = os.path.splitext(filename)[-1].split('.')[-1].lower()
    if not format or (format not in SUPPORT_FORMATS):
        raise Exception('Unsupported format!')

    return format
