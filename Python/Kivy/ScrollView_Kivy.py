from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self,tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa,font_size=30,size_hint_y=None,height=200))
class ScrollView_KV(App):
    def build(self):
        return Tarefas(['Tarefa1', 'Tarefa2','Tarefa1', 'Tarefa2','Tarefa1', 'Tarefa2','Tarefa1', 'Tarefa2'])

ScrollView_KV().run()