from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self,tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

class Tarefa(BoxLayout):
        def __init__(self,text='',**kwargs):
            super().__init__(**kwargs)
            self.ids.label.text = text

class Remove_Widgets_KV(App):
    def build(self):
        return Tarefas(['Tarefa1', 'Tarefa2','Tarefa1', 'Tarefa2','Tarefa1', 'Tarefa2','Tarefa1', 'Tarefa2'])

Remove_Widgets_KV().run()