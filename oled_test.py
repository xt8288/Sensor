#!/usr/bin/python3
import os

from PIL import ImageFont
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
serial = i2c(port=1, address=0x3C)
 
# substitute ssd1331(...) or sh1106(...) below if using that device
device = sh1106(serial)#这里改ssd1306, ssd1325, ssd1331, sh1106

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    print(font_path)
    return ImageFont.truetype(font_path, size)

fonts = [make_font("code2000.ttf", sz) for sz in range(24, 8, -2)]
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 20), "Hello World", fonts, fill="white")
