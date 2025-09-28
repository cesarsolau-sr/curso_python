class Producto:

    def __init__(self,nombre,precio,cantidad):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nombre
        if float(precio) < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = float(precio)
        if int(cantidad) < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = int(cantidad)    


    def actualizar_precio(self,new_precio):
        if new_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = new_precio

    def actualizar_cantidad(self, new_cantidad):
        if new_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = new_cantidad

    def calcular_valor_total(self):
        return self.cantidad * self.precio
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
    
class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto: 
            self.productos.append(producto)
    
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None
    
    def calcular_valor_inventario(self):
        total = 0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        return total
    
    def listar_productos(self):
        for producto in self.productos:
            print(producto.nombre)
    
    def menu_principal(self):
        opcion = 0
        while opcion == 0:
            print("Por favor seleccione una de las siguientes opciones:")
            print("1. agregar producto")
            print("2. Buscar Producto")
            print("3. Calcular valor del inventario")
            print("4. Listar productos")
            print("5. Salir")
            print("Ingrese su opción")
            try:
                op_usuario = int(input())
                match op_usuario:
                    case 1:
                        print("Digite el nombre del producto")
                        nombre = input()
                        print("Digite el precio del producto")
                        precio = input()
                        print("Digite la cantidad")
                        cantidad = input()
                        p = Producto(nombre,precio,cantidad)
                        self.agregar_producto(p)
                        #opcion = 0  
                    case 2:
                        print("Digite el producto a buscar")
                        nombre = input()
                        p = self.buscar_producto(nombre)
                        print(p.__str__())
                        #opcion = 0
                    case 3:
                        total = self.calcular_valor_inventario()
                        print(f"el valor total del inventario es: {total}")
                        #opcion = 0
                    case 4:
                        self.listar_productos()
                    case 5:
                        opcion = 1
            except ValueError:
                print("La entrada es incorrecta: escribe un numero entero")
                opcion = 0

        

if __name__ == "__main__":
    inv = Inventario()
    inv.menu_principal()
