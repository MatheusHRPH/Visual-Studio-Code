from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (400,600)

Builder.load_file('Tela.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.txtCalc.text = '0'

    #Create a button pressing function
    def ButtonPress(self, button):
        prior = self.ids.txtCalc.text  # Pega o que tem no TextInput

        if "Error" in prior:
            prior = ''

        if prior == "0":                # Verifica se é 0
            self.ids.txtCalc.text = ''
            self.ids.txtCalc.text = f'{button}'
        
        else:
            self.ids.txtCalc.text = f'{prior}{button}'

    #Create decimal function
    def Dot(self):
        prior = self.ids.txtCalc.text 
        number_list = prior.split("+")
        
        if "+" in prior and "." not in number_list[-1]:
            prior = f'{prior}.'
            self.ids.txtCalc.text = prior  
        
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.txtCalc.text = prior
    
    #Create function to remove last character
    def Remove(self):
        prior = self.ids.txtCalc.text
        prior = prior[:-1]
        self.ids.txtCalc.text = prior


    def Pos_Neg(self):
        prior = self.ids.txtCalc.text
        if "-" in prior:
            self.ids.txtCalc.text = f'{prior.replace("-", "")}'
        
        else:
           self.ids.txtCalc.text = f'-{prior}'


    #Create adition function
    def MathSign(self,sign):
        prior = self.ids.txtCalc.text
        # Slap a plus sign to the TextBox
        self.ids.txtCalc.text = f'{prior}{sign}'

   
    def Equals(self):
        prior = self.ids.txtCalc.text
        #Error Handling
        try:
            answer = eval(prior) 
            self.ids.txtCalc.text = str(answer)
        except:
            self.ids.txtCalc.text = ("Error")
        
        '''
        #Addition
        if "+" in prior:
            number_list = prior.split("+")
            answer = 0.0
            #Loop thru our list
            for number in number_list:
                answer = answer + float(number)

            self.ids.txtCalc.text = str(answer)
        '''




class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
CalculatorApp().run()