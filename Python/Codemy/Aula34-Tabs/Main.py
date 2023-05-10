from kivy.app import App    
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('Tela.kv')

class MyLayout(TabbedPanel):
    pass

class MyApp(App):
   def build(self):
       return MyLayout()
   
MyApp().run()
