import sqlite3

def connect_db():
  return sqlite3.connect('data/asistencia.db')

def create_table():
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS Alumnos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL)''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS Sesiones (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha TEXT NOT NULL)''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS Asistencias (
                        sesion_id INTEGER,
                        alumno_id INTEGER,
                        asistio INTEGER DEFAULT 0,
                        PRIMARY KEY (sesion_id, alumno_id))''')
  conn.commit()
  conn.close()

create_table()

def add_alumno(nombre):
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute('''INSERT INTO Alumnos (nombre) VALUES (?)''', (nombre,))
  conn.commit()
  conn.close()

def get_alumnos():
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute('''SELECT * FROM Alumnos''')
  alumnos = cursor.fetchall()
  conn.close()
  return alumnos