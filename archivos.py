import csv
import json
def guardar_csv(nombre_archivo, encabezados, datos):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=";")
        escritor.writerow(encabezados)
        for fila in datos:
            escritor.writerow(fila)
def cargar_csv_guardado(nombre_archivo):
    datos = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=";")

        for fila in lector:
            datos.append(fila)
    return datos
def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
def cargar_json(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
def mostrar_historial():
    try:
        with open("historial.csv", "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            historial = []
            for fila in lector:
                historial.append(fila)
            return historial
    except FileNotFoundError:
        return []
def guardar_resultado(resultado, nombre, tipo):
    if tipo == "json":
        guardar_json(nombre + ".json", resultado)
    elif tipo == "csv":
        datos_csv = []
        # Resultado tipo diccionario
        if type(resultado) == dict:
            for clave, valor in resultado.items():
                # Comparaciones
                if type(valor) == dict:
                    fila = [clave]
                    for dato in valor.values():
                        fila.append(dato)
                    datos_csv.append(fila)
                # Estadísticas o agrupaciones
                else:
                    datos_csv.append([clave, valor])
            guardar_csv(
                nombre + ".csv",
                ["CLAVE", "VALOR"],
                datos_csv
            )
        # Resultado tipo lista (búsquedas)
        elif type(resultado) == list:
            guardar_csv(
                nombre + ".csv",
                [],
                resultado
            )
