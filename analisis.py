def cargar_datos(nombre_archivo):
    datos = []
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(";")
        datos.append(partes)
    archivo.close()
    return datos


def buscar(datos, termino):
    resultados = []
    
    for fila in datos:
        texto = " ".join(fila)
        
        if termino.lower() in texto.lower():
            resultados.append(fila)
    
    print("Se encontraron", len(resultados), "registros")
    print("============================")

    for r in resultados:
        print(r)


def estadisticas(datos):
    valores = []
    
    for fila in datos[1:]:
        valores.append(float(fila[3]))
    
    maximo = valores[0]
    minimo = valores[0]
    suma = 0
    
    for v in valores:
        if v > maximo:
            maximo = v
        if v < minimo:
            minimo = v
        suma += v
    
    promedio = suma / len(valores)

    print("Datos de edad de los vehiculos")
    print("Máximo:", maximo, "Años")
    print("Mínimo:", minimo, "Años")
    print("Promedio:", promedio, "Años")

def agrupar_por_tipo(datos):
    conteo = {}
    
    for fila in datos[1:]:
        tipo = fila[2]
        
        if tipo in conteo:
            conteo[tipo] += 1
        else:
            conteo[tipo] = 1
    print("Tipo de vehiculo:")
    for tipo, cantidad in conteo.items():
        print(tipo, ":", cantidad)