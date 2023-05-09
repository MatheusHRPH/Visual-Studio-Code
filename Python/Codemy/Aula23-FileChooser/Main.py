from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            #print(filename[0])
        except:
            pass

class MyApp(App):
    def build(self):
        return MyLayout()
    
MyApp().run()
