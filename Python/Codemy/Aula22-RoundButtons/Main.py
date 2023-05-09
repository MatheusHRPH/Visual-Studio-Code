from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Builder.load_file('Tela.kv')

class MyLayout(Widget):
        pass

class MyApp(App):
        def build(self):
                Window.clearcolor = (1,1,1,1)
                return MyLayout()

MyApp().run()       
