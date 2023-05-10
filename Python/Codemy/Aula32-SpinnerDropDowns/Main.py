from kivy.app import App    
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = value

class MyApp(App):
   def build(self):
       return MyLayout()
   
MyApp().run()
