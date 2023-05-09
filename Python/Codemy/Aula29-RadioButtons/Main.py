from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    checks = []  
    def checkboxClick(self, instance, value, topping):
        if value == True:
            MyLayout.checks.append(topping)
            tops = ''
            for x in MyLayout.checks:
                tops = f'{tops} {x}'
            self.ids.lblOutput.text = f'You selected {tops}'
            if MyLayout.checks == []:
                self.ids.lblOutput.text = ''
        else:
            tops = ''
            for x in MyLayout.checks:
                tops = f'{tops} {x}'
            MyLayout.checks.remove(topping)
            self.ids.lblOutput.text = f'You selected {tops}' 
            if MyLayout.checks == []:
                self.ids.lblOutput.text = ''

class MyApp(App):  
    def build(self):
        return MyLayout()
    
MyApp().run()