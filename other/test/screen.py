from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.screenmanager import *

Builder.load_string("""
<MenuScreen>:
	BoxLayout:
		Button:
			text: 'Goto settings'
			on_press: root.manager.current = 'settings'
		Button:
			text: 'Quit'

<SettingsScreen>:
	BoxLayout:
		Button:
			text: 'My settings button'
		Button:
			text: 'Back to menu'
			on_press: root.manager.current = 'menu'
""")

class MenuScreen(Screen):
	pass


class SettingsScreen(Screen):
	pass

#sm=ScreenManager()
#sm=ScreenManager(transition=FadeTransition())
#sm=ScreenManager(transition=SwapTransition())
sm=ScreenManager(transition=SlideTransition(direction='down'))
#sm=ScreenManager(transition=WipeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))


class TestApp(App):
	def build(self):
		return sm


if __name__=='__main__':
	TestApp().run()
