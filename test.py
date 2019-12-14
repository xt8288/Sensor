#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

from PIL import ImageFont
from luma.core.render import canvas

from demo_opts import get_device


def stats(device):
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                'fonts', 'code2000.ttf'))
    font2 = ImageFont.truetype(font_path, 19)
    with canvas(device) as draw:
        draw.text((30, 25), '幻尔科技', font=font2, fill="white")
        

if __name__ == "__main__":
    try:
        device = get_device()        
    except KeyboardInterrupt:
        pass
    while True:
        stats(device)
        time.sleep(100)
