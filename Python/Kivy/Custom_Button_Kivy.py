from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
import json
from kivy.core.audio import SoundLoader
from kivy.metrics import sp

class Gerenciador(ScreenManager):
    pass
class Menu(Screen):
    poppSound = None
    
    def on_pre_enter(self):
         Window.bind(on_request_close=self.confirmacao)
         if self.poppSound == None:
            self.poppSound = SoundLoader.load('pare.mp3')
            
    def confirmacao(self, *args, **kwargs):   
        self.poppSound.play()
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10,spacing=10)
        pop = Popup(title='Deseja mesmo sair?',content=box,size_hint=(None,None),size=(150,150))
        
        sim = Botao(text = 'Sim',on_release=(App.get_running_app().stop))
        nao = Botao(text = 'Nao',on_release=pop.dismiss)
        
        botoes.add_widget(sim)
        botoes.add_widget(nao)
        
        atencao = Image(source = 'atencao.png')
        
        box.add_widget(atencao)
        box.add_widget(botoes)

        animSim = Animation(color=(0,0,0,1)) + Animation(color=(1,1,1,1))
        animSim.repeat = True
        animSim.start(sim)
        
        anim = Animation(size=(300,180),duration=0.2,t='out_back')
        anim.start(pop)
        pop.open()
        return True

class Botao(ButtonBehavior,Label):
    cor = ListProperty([0.1,0.5,0.7,1])
    cor2 = ListProperty([0.1,0.1,0.1,1])

    def __init__(self,**kwargs):
            super(Botao,self).__init__(**kwargs)
            self.atualizar()
    def on_kv_post(self, base_widget):
         return super().on_kv_post(base_widget)
    def on_pos(self,*args):
        self.atualizar()
    
    def on_size(self,*args):
        self.atualizar()

    def on_press(self,*args):
        self.cor,self.cor2 = self.cor2,self.cor
    
    def on_release(self, *args):
        self.cor,self.cor2 = self.cor2,self.cor  
       
    def on_cor(self,*args):
        self.atualizar()
    def atualizar(self,*args):
            self.canvas.before.clear()
            with self.canvas.before:
                Color(rgba=self.cor)
                Ellipse(size=(self.height,self.height),pos=self.pos)
                Ellipse(size=(self.height,self.height),pos=(self.x+self.width-self.height,self.y))
                Rectangle(size=(self.width-self.height,self.height),pos=(self.x+self.height/2.0,self.y))


class Tarefas(Screen):
    tarefas = []
    path = ''
   
    def on_pre_enter(self):
        self.ids.box.clear_widgets()
             
        self.path = App.get_running_app().user_data_dir+'/'
        self.loadData()
        Window.bind(on_keyboard=self.voltar)
        for tarefa in self.tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)
    
    def loadData(self,*args):
        try:
            with open(self.path + 'data.json', 'r') as data:
                self.tarefas = json.load(data)
        except FileNotFoundError:
            pass

    def saveData(self,*args):
        with open(self.path + 'data.json', 'w') as data:
            json.dump(self.tarefas,data)

    def addWidget(self):
        global popSound
        popSound.play()
        texto = self.ids.textotarefa.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.textotarefa.text=''
        self.tarefas.append(texto)
        self.saveData()

    def removeWidget(self,tarefa):
        global poprSound
        poprSound.play()
        texto = tarefa.ids.label.text
        self.ids.box.remove_widget(tarefa)
        self.tarefas.remove(texto)
        self.saveData()

    def confirmacao(self, *args):
        global poppSound
        poppSound.play()
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10,spacing=10)
        pop = Popup(title='Deseja mesmo sair?',content=box,size_hint=(None,None),size=(300,180))
        
        sim = Botao(text = 'Sim',on_release=App.get_running_app().stop)
        nao = Botao(text = 'Nao',on_release=pop.dismiss)
        
        botoes.add_widget(sim)
        botoes.add_widget(nao)
        
        atencao = Image(source = 'atencao.png')

        box.add_widget(atencao)
        box.add_widget(botoes)
        
        pop.open()

class Mensagem(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1,None)
        self.font_size = sp(30)    
    def on_size(self,*args):
        self.text_size = (self.width - sp(10), None)

    def on_texture_size(self,*args):
        self.size = self.texture_size
        self.height += sp(20)          
  

class Tarefa(BoxLayout):
        def __init__(self,text='',**kwargs):
            super().__init__(**kwargs)
            self.ids.label.text = text
                

class Custom_Button_KV(App):
    def build(self):
            return Gerenciador()
popSound = SoundLoader.load('xaropinho.mp3')
poprSound = SoundLoader.load('tome.mp3')
poppSound = SoundLoader.load('pare.mp3')
Custom_Button_KV().run()
