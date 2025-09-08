class Biblioteca:
    total_libros  = 0
    nombre_biblioteca  = 'Biblioteca Central'

    def __init__(self,nombre_seccion ):
        self.nombre_seccion = nombre_seccion
        self.libros = []

 
    def agregar_libro(self, titulo):
        self.libros.append(titulo)
        Biblioteca.total_libros += 1

    def obtener_informe(self):
        return f"Sección {self.nombre_seccion} de {self.nombre_biblioteca}: {Biblioteca.total_libros} libros"
    
b1 = Biblioteca("Misterio")
b1.agregar_libro("Delirio")
#Biblioteca.total_libros += 1
b1.agregar_libro("Manual de Usuario")
#Biblioteca.total_libros += 1
print(b1.obtener_informe())

b2 = Biblioteca("Naturaleza")
b2.agregar_libro("botanica")
#Biblioteca.total_libros += 1
b2.agregar_libro("Herbolario de Hosho")
#Biblioteca.total_libros += 1
print(b2.obtener_informe())
