from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.student_screen import StudentScreen
from kivy.lang import Builder
import os
from kivy.config import Config

Config.set('graphics', 'width', '380')
Config.set('graphics', 'height', '640')

class AsistenciaApp(App):
  def build(self):
    # kv_folder = 'screens/kv'
        
    # for filename in os.listdir(kv_folder):
    #     if filename.endswith('.kv'):
    #         Builder.load_file(os.path.join(kv_folder, filename))
    Builder.load_file('screens/kv/navigation_bar.kv')
    Builder.load_file('screens/kv/home_screen.kv')
    Builder.load_file('screens/kv/student_screen.kv')
    Builder.load_file('main.kv')
    sm = ScreenManager()
    sm.add_widget(HomeScreen(name='home'))
    sm.add_widget(StudentScreen(name='student'))
    return sm

if __name__ == '__main__':
  AsistenciaApp().run()