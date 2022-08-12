from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass
class Menu(Screen):
    pass

class Tarefas(Screen):
    def __init__(self,tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
    def addWidget(self):
        texto = self.ids.textotarefa.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.textotarefa.text=''

class Tarefa(BoxLayout):
        def __init__(self,text='',**kwargs):
            super().__init__(**kwargs)
            self.ids.label.text = text

class Menu_Image_KV(App):
    def build(self):
        return Gerenciador()
Menu_Image_KV().run()


