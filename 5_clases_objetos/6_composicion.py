class Libro:

    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}"

class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        encontrados = []
        for libro in self.libros:
            if titulo in libro.titulo:
                encontrados.append(libro)
        return encontrados
    
    def contar_libros_autor(self, autor):
        cont = 0
        for libro in self.libros:
            if libro.autor == autor:
                cont += 1 
        return cont

l1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
l2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
l3 = Libro("El Amor en los Tiempos del Cólera", "Gabriel García Márquez", 1985) 
l4 = Libro("La Sombra del Viento", "Carlos Ruiz Zafón", 2001)

biblo = Biblioteca()
biblo.agregar_libro(l1)
biblo.agregar_libro(l2)
biblo.agregar_libro(l3)
biblo.agregar_libro(l4)

libros = biblo.buscar_libro("Cien Años de Soledad")
for libro in libros:
    print(libro)
print(biblo.contar_libros_autor("Gabriel García Márquez"))