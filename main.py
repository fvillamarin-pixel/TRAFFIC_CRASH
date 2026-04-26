from analisis import cargar_datos, buscar, estadisticas, agrupar_por_tipo


def menu():
    datos = cargar_datos("TRAFFIC_CRASHpequeño.csv")
    while True:
        print("====== MENÚ DATA LAB ======")
        print("1. Buscar registros")
        print("2. Estadísticas")
        print("3. Agrupar por tipo")
        print("4. Salir")
        print("============================")
        opcion = input("Seleccione una opción: ")
        print("============================")
        if opcion == "1":
            termino = input("Ingrese término: ")
            buscar(datos, termino)
        elif opcion == "2":
            estadisticas(datos)
        elif opcion == "3":
            agrupar_por_tipo(datos)
        elif opcion == "4":
            break
        else:
            print("Opción inválida", "\nDigite un opcion valida")


menu()