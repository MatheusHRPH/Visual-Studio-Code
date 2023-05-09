from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    def slide_it(self,*args):
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1]))
        # print(args[1])
    

class MyApp(App):
    def build(self):
        return MyLayout()
    
MyApp().run()