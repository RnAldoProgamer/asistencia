from kivy.uix.screenmanager import Screen
from kivy.uix.camera import Camera
# from screens.manage_screen import ManageScreen
# from screens.edit_screen import EditScreen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
    
    """ def start_scan(self, instance):
        self.manager.current = 'manage'
        self.manager.get_screen('manage').bind(on_enter=self.update_alumnos_list)
        
        camera = Camera(resolution=(640, 480), play=True)
        camera.bind(on_load=self.on_load)
        camera.bind(on_error=self.on_error) """
    
    def go_to_student(self, instance):
        self.manager.current = 'student'
    
    def on_load(self, instance):
        self.manager.current = 'manage'
        self.manager.get_screen('manage').bind(on_enter=self.update_alumnos_list)
    
    def on_error(self, instance):
        self.manager.current = 'manage'
        self.manager.get_screen('manage').bind(on_enter=self.update_alumnos_list)
        
    def go_to_home(self, instance):
        self.manager.current = 'home'
    
    def go_to_report(self, instance):
        self.manager.current = 'report'
    
    def go_to_settings(self, instance):
        self.manager.current = 'settings'