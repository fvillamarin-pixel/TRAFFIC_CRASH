import csv
from datetime import datetime
def cargar_datos(nombre_archivo):
    datos = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        for fila in lector:
            datos.append(fila)
    return datos
def registrar_historial(consulta, cantidad_resultados):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("csvs/historial.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([fecha, consulta, cantidad_resultados])
def buscar(datos, termino):
    resultados = []
    for fila in datos[1:]:
        texto = " ".join(fila)
        if termino.lower() in texto.lower():
            resultados.append(fila)
    registrar_historial(f"Búsqueda: {termino}", len(resultados))
    return resultados
def estadisticas(datos):
    valores = []
    for fila in datos[1:]:
        try:
            valores.append(float(fila[3]))
        except:
            pass
    maximo = max(valores)
    minimo = min(valores)
    promedio = sum(valores) / len(valores)
    resultado = {
        "maximo": maximo,
        "minimo": minimo,
        "promedio": round(promedio, 2)
    }
    registrar_historial("Estadísticas de edad", 1)
    return resultado
def agrupar_por_tipo(datos):
    conteo = {}
    for fila in datos[1:]:
        tipo = fila[2]
        if tipo in conteo:
            conteo[tipo] += 1
        else:
            conteo[tipo] = 1
    registrar_historial("Agrupar por tipo", len(conteo))
    return conteo
def comparar_grupos(datos, columna, grupo1, grupo2):
    columnas = {
        "marca": 0,
        "modelo": 1,
        "tipo": 2
    }
    indice = columnas[columna]
    cantidad1 = 0
    cantidad2 = 0
    suma1 = 0
    suma2 = 0
    for fila in datos[1:]:
        # Validar tamaño de fila
        if len(fila) < 4:
            continue
        valor = fila[indice].strip().upper()
        try:
            edad = float(fila[3])
        except:
            continue
        if valor == grupo1.strip().upper():
            cantidad1 += 1
            suma1 += edad
        elif valor == grupo2.strip().upper():
            cantidad2 += 1
            suma2 += edad
    promedio1 = 0
    promedio2 = 0
    if cantidad1 > 0:
        promedio1 = round(suma1 / cantidad1, 2)
    if cantidad2 > 0:
        promedio2 = round(suma2 / cantidad2, 2)
    return {
        grupo1: {
            "cantidad": cantidad1,
            "promedio_edad": promedio1
        },
        grupo2: {
            "cantidad": cantidad2,
            "promedio_edad": promedio2
        }
    }
def mostrar_valores_unicos(datos, columna):
    columnas = {
        "marca": 0,
        "modelo": 1,
        "tipo": 2
    }
    indice = columnas[columna]
    valores = set()
    for fila in datos[1:]:
        if len(fila) > indice:
            valor = fila[indice].strip()
            if valor != "":
                valores.add(valor)
    return sorted(valores)
