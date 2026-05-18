from analisis import (
    cargar_datos,
    buscar,
    estadisticas,
    agrupar_por_tipo,
    comparar_grupos,
    mostrar_valores_unicos
)
from archivos import (
    guardar_csv,
    guardar_json,
    cargar_csv_guardado,
    cargar_json,
    mostrar_historial,
    guardar_resultado
)
def imprimir_resultados(resultados):
    for fila in resultados:
        print(fila)
def menu():
    datos = cargar_datos("TRAFFIC_CRASHpequeño.csv")
    while True:
        print("\n====== MENÚ DATA LAB ======")
        print("1. Buscar registros")
        print("2. Estadísticas")
        print("3. Agrupar por tipo")
        print("4. Comparar grupos")
        print("5. Ver historial")
        print("6. Cargar archivo guardado")
        print("7. Salir")
        print("============================")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            termino = input("Ingrese término de búsqueda: ")
            resultados = buscar(datos, termino)
            print("\nSe encontraron", len(resultados), "registros")
            imprimir_resultados(resultados)
            guardar = input("\n¿Desea guardar los resultados? (s/n): ")
            if guardar.lower() == "s":
                tipo = input("Guardar como CSV o JSON: ").lower()
                if tipo == "csv":
                    guardar_csv(
                        "resultados_busqueda.csv",
                        datos[0],
                        resultados
                    )
                    print("Archivo CSV guardado correctamente")
                elif tipo == "json":
                    guardar_json(
                        "resultados_busqueda.json",
                        resultados
                    )
                    print("Archivo JSON guardado correctamente")
        elif opcion == "2":
            resultado = estadisticas(datos)
            print("\nDatos de edad de los vehículos")
            print("Máximo:", resultado["maximo"], "años")
            print("Mínimo:", resultado["minimo"], "años")
            print("Promedio:", resultado["promedio"], "años")
            guardar = input("\n¿Desea guardar las estadísticas? (s/n): ")
            if guardar.lower() == "s":
                tipo = input("Guardar como CSV o JSON: ").lower()
                nombre = input("Ingrese el nombre del archivo: ")
                guardar_resultado(
                    resultado,
                    nombre,
                    tipo
                )
                print("Archivo guardado correctamente")
        elif opcion == "3":
            conteo = agrupar_por_tipo(datos)
            print("\nCantidad por tipo de vehículo")
            for tipo, cantidad in conteo.items():
                print(tipo, ":", cantidad)
            guardar = input("\n¿Desea guardar las estadísticas? (s/n): ")
            if guardar.lower() == "s":
                tipo = input("Guardar como CSV o JSON: ").lower()
                nombre = input("Ingrese el nombre del archivo: ")
                guardar_resultado(
                    resultado,
                    nombre,
                    tipo
                )
                print("Archivo guardado correctamente")
        elif opcion == "4":
            print("\n¿Qué desea comparar?")
            print("1. Marca")
            print("2. Modelo")
            print("3. Tipo de vehículo")
            opcion_comparacion = input("Seleccione una opción: ")
            if opcion_comparacion == "1":
                columna = "marca"
            elif opcion_comparacion == "2":
                columna = "modelo"
            elif opcion_comparacion == "3":
                columna = "tipo"
            else:
                print("Opción inválida")
                continue
            print("\nValores disponibles:\n")
            valores = mostrar_valores_unicos(datos, columna)
            for valor in valores:
                print("-", valor)
            grupo1 = input("\nIngrese el primer valor: ")
            grupo2 = input("Ingrese el segundo valor: ")
            resultado = comparar_grupos(
                datos,
                columna,
                grupo1,
                grupo2
            )
            print("\n====== RESULTADOS ======")
            for grupo, info in resultado.items():
                print("\nGrupo:", grupo)
                print("Cantidad:", info["cantidad"])
                print("Promedio edad:", info["promedio_edad"])   
            guardar = input("\n¿Desea guardar las estadísticas? (s/n): ")
            if guardar.lower() == "s":
                tipo = input("Guardar como CSV o JSON: ").lower()
                nombre = input("Ingrese el nombre del archivo: ")
                guardar_resultado(
                    resultado,
                    nombre,
                    tipo
                )
                print("Archivo guardado correctamente")      
        elif opcion == "5":
            historial = mostrar_historial()
            print("\n====== HISTORIAL ======")
            if len(historial) == 0:
                print("No hay historial registrado")
            else:
                for registro in historial:
                    print(registro)
        elif opcion == "6":
            print("\n¿Qué tipo de archivo desea cargar?")
            print("1. CSV")
            print("2. JSON")
            tipo = input("Seleccione una opción: ")
            nombre = input("Ingrese el nombre del archivo: ")
            if tipo == "1":
                try:
                    datos_guardados = cargar_csv_guardado(
                        nombre + ".csv"
                    )
                    print("\nArchivo CSV cargado correctamente")

                    for fila in datos_guardados:
                        print(fila)

                except:
                    print("No se pudo cargar el archivo")
            elif tipo == "2":
                try:
                    datos_guardados = cargar_json(
                        nombre + ".json"
                    )
                    print("\nArchivo JSON cargado correctamente")
                    print(datos_guardados)
                except:
                    print("No se pudo cargar el archivo")
            else:
                print("Opción inválida")
menu()
