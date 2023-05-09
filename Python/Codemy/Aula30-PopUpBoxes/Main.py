from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyLayout()
    
MyApp().run() 