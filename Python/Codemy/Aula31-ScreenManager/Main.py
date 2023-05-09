from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

#Define our different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):

KV = Builder.load_file('Tela.kv')


class MyApp(App):
    def build(self):
        return KV
    
MyApp().run() 