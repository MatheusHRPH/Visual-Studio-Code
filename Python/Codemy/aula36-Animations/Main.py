from kivy.app import App    
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0,0,1,1),
            duration = 0.2,
            
        )
        #Second animation
        animate += Animation(size_hint=(1,1))
        #Star the animation
        animate.start(widget)

        #Create a callback
        animate.bind(on_complete = self.my_callback)

    def my_callback(self,*args):
        self.ids.lblTexto.text = "Terminou"
class MyApp(App):
   def build(self):
       return MyLayout()
   
MyApp().run()
