from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty

from ScreenOne import ScreenOneView
from ScreenTwo import ScreenTwoView
from ScreenThree import ScreenThreeView

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Carregar arquivos kv
        self.load_all_kv_files(self.directory)
        # Gerenciador de telas
        self.sm = MDScreenManager()

    def build(self):
        self.sm.add_widget(ScreenOneView())
        self.sm.add_widget(ScreenTwoView())
        self.sm.add_widget(ScreenThreeView())

        return self.sm


MainApp().run()
