# from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from database.database_manager import get_alumnos
import qrcode
import os

class ManageScreen:
  def __init__(self, **kwargs):
    super(ManageScreen, self).__init__(**kwargs)
    self.layout = BoxLayout(orientation='vertical')
    
    add_button = Button(text='Añadir alumno', size_hint=(1, 0.1), pos_hint={'center_x': 0.5})
    add_button.bind(on_press=self.add_alumno)
    self.layout.add_widget(add_button)
    
    self.alumnos_list = ScrollView(size_hint=(1, 0.8))
    self.update_alumnos_list()
    self.layout.add_widget(self.alumnos_list)
    
    self.add_widget(self.layout)
  
  def update_alumnos_list(self):
    alumnos = get_alumnos()
    list_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.8))
    list_layout.bind(minimum_height=list_layout.setter('height'))
    
    for alumno in alumnos:
      alumno_id, nombre = alumno
      item = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
      item.add_widget(Label(text=nombre, size_hint=(1, 0.8)))
      edit_button = Button(text='Editar', size_hint=(1, 0.1), pos_hint={'center_x': 0.5})
      edit_button.bind(on_press=lambda x, y=alumno_id: self.edit_alumno(y))
      item.add_widget(edit_button)
      qr_button = Button(text='Ver QR', size_hint=(1, 0.1), pos_hint={'center_x': 0.5})
      qr_button.bind(on_press=lambda x, y=alumno_id: self.show_qr(y))
      item.add_widget(qr_button)
      list_layout.add_widget(item)
    
    self.alumnos_list.clear_widgets()
    self.alumnos_list.add_widget(list_layout)
  
  def go_to_add(self, instance):
    self.manager.current = 'edit'
  
  def go_to_edit(self, alumno_id):
    self.manager.get_screen('edit').alumno_id = alumno_id
    self.manager.current = 'edit'
  
  def show_qr(self, alumno_id):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(str(alumno_id))
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    qr_path = f"temp_qr_{alumno_id}.png"
    qr_img.save(qr_path)
    
    popup_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
    qr_image = Image(source=qr_path, size_hint=(1, 1))
    popup_layout.add_widget(qr_image)
    close_button = Button(text='Cerrar', size_hint=(1, 0.1), pos_hint={'center_x': 0.5})
    popup_layout.add_widget(close_button)
    
    
    popup = Popup(title=f'QR del alumno {alumno_id}', content=popup_layout, size_hint=(1, 1))
    close_button.bind(on_press=popup.dismiss)
    popup.open()
    
    close_button.bind(on_press=lambda x: os.remove(qr_path) if os.path.exists(qr_path) else None)