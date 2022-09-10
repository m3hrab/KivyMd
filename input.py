from kivy.app import App 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class InputApp(App):

    def build(self):
        self.layout = GridLayout(cols=2, row_force_default = True, row_default_height = 50, spacing= 10, padding= 40)
        self.w = TextInput(text="", multiline = False)
        self.h = TextInput(text="", multiline = False)
        submit = Button(text="Calculate", on_press = self.calculate)

        self.layout.add_widget(self.w)
        self.layout.add_widget(self.h)
        self.layout.add_widget(submit)
        
        return self.layout

    def calculate(self, obj):
        value = int(self.w)*int(self.h)
        n = "Area: " + str(value) 
        self.layout.add_widget(Label(text=n))


InputApp().run()