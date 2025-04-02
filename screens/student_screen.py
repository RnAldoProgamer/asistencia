from kivy.uix.screenmanager import Screen

class StudentScreen(Screen):
  def __init__(self, **kwargs):
    super(StudentScreen, self).__init__(**kwargs)
    
  def go_to_home(self, instance):
    self.manager.current = 'home'
  
  def go_to_student(self, instance):
    self.manager.current = 'student'
  
  def go_to_report(self, instance):
    self.manager.current = 'report'
  
  def go_to_settings(self, instance):
    self.manager.current = 'settings'