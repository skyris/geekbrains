#!/usr/bin/env python3

from __future__ import print_function
import sys
from PIL import Image

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            if im.size[0]/im.size[1] == 1.5:
                print(infile, im.format, "%dx%d" % im.size, im.mode)
    except IOError:
        pass
