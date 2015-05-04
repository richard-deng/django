#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image,ImageFont,ImageDraw
import random
import math
#width
width=1024
#height
height=820
#color
bgcolor=(0,128,192)
image=Image.new('RGB',(width,height),bgcolor)
font=ImageFont.truetype('huakang.ttf',100)
fontcolor=(0,255,0)
draw=ImageDraw.Draw(image)
draw.text((100,300),u"马丽，超级玛丽!",font=font,fill=fontcolor)
image.save('mali.png')
