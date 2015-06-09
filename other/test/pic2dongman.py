#-*- coding: utf-8  -*-

import glob, os, time
from PIL import Image

class Text(object):
    def __init__(self, inputdir):
        self.inputdir=inputdir
        self.piclist=glob.glob(self.inputdir+os.path.sep+'*.png')
        self.piclist=sorted(self.piclist, key=os.path.getmtime)


    def pictotext(self, picpath):
        pic=Image.open(picpath)
        pic=pic.resize((60,40))
        pic=pic.convert('L')
        width, height=pic.size
        text=""
        pix=pic.load()
        for row in xrange(height):
            for col in xrange(width):
                if int(pix[col,row])<128:
                    text+='#'
                else:
                    text+=' '
            text+='\n'
        return text

    def pictotextnew(self, picpath):
        pic=Image.open(picpath)
        pic=pic.resize((60,40))
        pic=pic.convert('L')
        width, height=pic.size
        text=""
        data={}
        pix=pic.load()
        for row in xrange(height):
            for col in xrange(width):
                if int(pix[col,row])<128:
                    text+='#'
                else:
                    text+=' '
            text+='\n'
            data[str(row)]=text
            text = ""
        return data

def main():
    path='.'
    display=Text(path)
    need_str={}
    choice=raw_input('play it or not y/n?\n')
    if choice is 'y':
        for i in display.piclist:
            time.sleep(1)
            os.system('clear')
            char=display.pictotext(i)
            need_str[str(i)]=char
            print char

def test(name):
    #path='fbb5.jpg'
    path=name
    display=Text(path)
    char=display.pictotextnew(path)

    #print char
    return char
    

if __name__ == '__main__':
    #a=test()
    #f=open('fbb5.txt','w')
    #f.write(a)
    #f.close()
    main()
