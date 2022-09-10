from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

class mainApp(MDApp):

    def build(self):
        text = MDLabel(text="Hello World",halign="center")
        return text

mainApp().run()