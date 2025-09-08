class Libro:
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def describir(self):
        return f"{self.titulo} escrito por {self.autor}-{self.paginas} páginas"

    def es_largo(self):
        if self.paginas > 300:
            return True
        else:
            return False
            
    def resumir(self,longitud=50):
        return f"{self.titulo} - Resumen de {longitud} caracteres"

libro1 = Libro("El amanecer","Cess Solano",250)
print(libro1.describir())
print(libro1.es_largo())
print(libro1.resumir())

libro2 = Libro("Maria Fernanda", "MaFe", 500)
print(libro2.describir())
print(libro2.es_largo())
print(libro2.resumir(400))