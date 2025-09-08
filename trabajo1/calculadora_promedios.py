def ingresar_calificaciones():
    continuar = "Si"
    lista_materias=[]  
    lista_calificaciones=[]
    #permite iterar para ingresar n materias mientras la variables sea SI
    while continuar == "Si":
        m_validar = True
        #itera hasta recibir una materia que no sea vacía
        while m_validar:
            print("Por favor ingrese su materia")
            materia = input()  
            #valida que el nombre de la materia no este vacio
            if materia != "":      
                lista_materias.append(materia)
                m_validar = False
            else:
                print("materia invalida")
                m_validar = True
        entero = True
        while entero:
            print("Por favor ingrese su calificación")
            calificacion = input()
            entero = calificacion_valida(calificacion)
            if entero:
                lista_calificaciones.append(float(calificacion))
                entero = False
            else:    
                print("La calificación no es valida")
                entero = True
        print("Desea ingresar otra materia, digite Si, de lo contrario presione cualquier tecla")
        continuar = input()
    return lista_materias, lista_calificaciones

def calificacion_valida(cal):
    try:
        num = float(cal)
        if (num >= 0 and num <= 10):
            return True
        else:
            return False
    except ValueError:
        return False

def calcular_promedio(calificaciones):
    sum = 0
    for c in calificaciones:
        sum += c
    promedio = sum/len(calificaciones)
    return promedio

def determinar_estado(calificaciones, umbral) :
    aprobadas = []
    reprobadas= []
    for index, cal in enumerate(calificaciones):
        if cal > umbral:
            aprobadas.append(index)
        else:
            reprobadas.append(index)
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    # Encontrar el valor mínimo y su índice
    valor_minimo = min(calificaciones)
    indice_minimo = calificaciones.index(valor_minimo)

    # Encontrar el valor máximo y su índice
    valor_maximo = max(calificaciones)
    indice_maximo = calificaciones.index(valor_maximo)
    return indice_maximo, indice_minimo

#metodo main
if __name__ == "__main__":
    materias, calificaciones = ingresar_calificaciones()
    for m, c in zip(materias, calificaciones):
        print(f"materia:{m} calificación:{c}")
    promedio = calcular_promedio(calificaciones)
    print(f"promedio de las calificaciones: {promedio}")
    aprobadas, reprobadas = determinar_estado(calificaciones,5.0)
    for a in aprobadas:
        print(f"materia aprobada:{materias[a]}")
    for b in reprobadas:
        print(f"materia reprobadas:{materias[b]}")
    m_alta, m_baja = encontrar_extremos(calificaciones)
    print(f"materia calificacion mas alta: {materias[m_alta]}")
    print(f"materia calificacion mas baja: {materias[m_baja]}")
    print("finalzación del programa, buen día")        