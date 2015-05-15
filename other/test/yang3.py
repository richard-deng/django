#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image,ImageFont,ImageDraw
import random
import math
import time
#width
width=1280
#height
height=800
#color
bgcolor=(0,128,192)
image=Image.new('RGB',(width,height),bgcolor)
font=ImageFont.truetype('huakang.ttf',100)
fontcolor=(0,255,0)
draw=ImageDraw.Draw(image)
draw.text((300,400),u"寄不出去的感情",font=font,fill=fontcolor)
image.save('feeling.png')


#data=[
#	{'key1':u'衣带渐宽终不悔','key2':u'为伊消得人憔悴'},
#	{'key1':u'两情若是久长时','key2':u'又岂能朝朝暮暮'},
#	{'key1':u'相思相见知何日','key2':u'此时此夜难为情'},
#	{'key1':u'曾经沧海难为水','key2':u'除却巫山不是云'},
#	{'key1':u'凄凉别后两应同','key2':u'最是不胜清怨月明中'},
#	{'key1':u'还君明珠双泪垂','key2':u'恨不相逢未嫁时'},
#	{'key1':u'嗟余只影系人间','key2':u'如何同生不同死'},
#
#	{'key1':u'相思树底说相思','key2':u'思郎恨郎郎不知'},
#	{'key1':u'相见争如不见','key2':u'有请何似无情'},
#	{'key1':u'相思相见知何日','key2':u'此时此夜难为情'},
#]
#
#i=0
#for item in data:
#    image=Image.new('RGB',(width,height),bgcolor)
#    draw=ImageDraw.Draw(image)
#    draw.text((300,200),item['key1'],font=font,fill=fontcolor)
#    draw.text((300,400),item['key2'],font=font,fill=fontcolor)
#    image.save('%s_s.png'%str(i))
#    i+=1
