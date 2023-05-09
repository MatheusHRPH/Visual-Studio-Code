from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.spelling import Spelling


Builder.load_file('Tela.kv')

class MyLayout(Widget):
    def press(self):
        #Create instance of Spelling
        s = Spelling()

        # Select the language
        s.select_language('en-US')

        # Grab the word from textbox
        word = self.ids.word_input.text
        x = ''
        for item in s.suggest(word):
            x = f'{x}\n{item}'
            self.ids.word_label.text = f'{x}'
        
        
class MyApp(App):
    def build(self):
        return MyLayout()
    
MyApp().run()