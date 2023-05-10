from kivy.app import App    
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    def hello(self):
        
        self.ids.myImage.source = 'Botao1.png'
    def pressBtn(self):
        self.ids.myImage.source = 'Botao2.png'
        self.ids.lblTexto.text= "AAA"
class MyApp(App):
   def build(self):
       return MyLayout()
   
MyApp().run()
