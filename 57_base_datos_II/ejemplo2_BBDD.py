import sqlite3

mi_conexion=sqlite3.connect('GestionProductos')

mi_cursor=mi_conexion.cursor()

mi_cursor.execute('''
  CREATE TABLE PRODUCTOS (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  NOMBRE_ARTICULO VARCHAR(50),
  PRECIO INTEGER,
  SECCION VARCHAR(20))
''')

productos=[
  ('pelota', 20, 'juguetería'),
  ('pantalón', 15, 'confección'),
  ('destornillador', 25, 'ferretería'),
  ('jarrón', 45, 'cerámica')
]
mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

mi_conexion.commit()

mi_conexion.close()