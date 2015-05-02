from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line,Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty
from kivy.core.window import Window
d = 3
class MyPaintWidget(Widget):
    
    def on_touch_down(self, touch):
	global d
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y),width=d)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
    
    def echo_touch(self):
        print self.width,self.height
    def doscreenshot(self,*largs):
        Window.screenshot(name='screenshot%(counter)04d.jpg')


class MyPaintApp(App):
    #def doscreenshot(self,*largs):
    #    Window.screenshot(name='screenshot%(counter)04d.jpg')

    def build(self):
        parent = Widget()
        painter = MyPaintWidget()
        boxglobal = BoxLayout(orientation='vertical',size_hint=(1,0.8),size=(200,80)) 
        boxlayout = BoxLayout(size_hint=(1,0.2))
        #with boxlayout.canvas.before:
        #    Color(1,0,1,mode='rgb')
        #    self.rect = Rectangle(size=boxlayout.size,pos=boxlayout.pos)
        
        clearbtn = Button(text='Clear')
        upbtn = Button(text='+')
        downbtn = Button(text='-')
        echobtn = Button(text='Save')
  
        boxlayout.add_widget(clearbtn)
        boxlayout.add_widget(upbtn)
        boxlayout.add_widget(downbtn)
        boxlayout.add_widget(echobtn)

        boxglobal.add_widget(painter)
        boxglobal.add_widget(boxlayout)
        #parent.add_widget(painter)
        parent.add_widget(boxglobal)
	

        def clear_canvas(obj):
            painter.canvas.clear()
	
        clearbtn.bind(on_release=clear_canvas)

        #echobtn.bind(on_press=self.doscreenshot)
        echobtn.bind(on_press=painter.doscreenshot)

        def up_width(obj):
            global d
            d = d+1
            print d
        upbtn.bind(on_release=up_width)
        
        def down_width(obj):
            global d
            d = d -1
            if d <= 0:
                d = 1
            print d
        downbtn.bind(on_release=down_width)
        return parent


if __name__ == '__main__':
    MyPaintApp().run()
