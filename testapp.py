from turtle import pos
from kivy.app import App 
from kivy.uix.label import Label 

class NewApp(App):

    def build(self):
        text = Label(text="Hello ", pos_hint={None, None}, pos=(23,23))
        return text

NewApp().run()