from cProfile import label
from cgitb import text
from imp import source_from_cache
from turtle import color, pos, width
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (368, 570)

class MainApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing="40sp", padding="80sp")
        img = AsyncImage(source = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtmaNC8EyHSCbnBPf1m5Kol8SXGRFcXgv19hNabFsd&s")
        btn4 = Button(text="Login", size_hint=(None, None), width="100sp", height="50sp", pos_hint={'center_x': .5,'center_y': 0.0})
        layout.add_widget(img)
        layout.add_widget(btn4)


        return layout

    
MainApp().run()