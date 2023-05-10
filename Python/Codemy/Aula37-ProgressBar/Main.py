from kivy.app import App    
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    def btnClick(self):
        current = self.ids.my_progress_bar.value

        #If to restart over after 100
        if current == 100:
            current = 0

        current += 25
        self.ids.my_progress_bar.value = current
        #Updatde the label
        self.ids.lblTexto.text = f'{int(current)}%   Progress'

class MyApp(App):
   def build(self):
       return MyLayout()
   
MyApp().run()