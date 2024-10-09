pacientes = []


def cargar_pacientes(cantidad_pacientes: int) -> list[list]:
    """Carga a una lista bidimensional de nombre `pacientes` 5 elementos a traves del metodo append()"""
    for i in range(cantidad_pacientes):
        cargar_n_historia_clinica = int(input("Ingrese el numero de historia clinica: "))
        cargar_nombre_paciente = input("Ingrese el nombre del paciente: ")
        cargar_edad_paciente = int(input("Ingrese la edad del paciente: "))
        cargar_diagnostico = input("Ingrese el diagnostico: ")
        cargar_dias_internacion = int(input("Ingrese la cantidad de dias de internacion: "))
        pacientes.append([cargar_n_historia_clinica, cargar_nombre_paciente, cargar_edad_paciente, cargar_diagnostico, cargar_dias_internacion])

def mostrar_pacientes() -> str:
    """Muestra la lista bidimensional `pacientes` fila por fila"""
    for paciente in pacientes:
        print(f"Paciente: {paciente}")

def buscar_pacientes_nhc() -> list[list]:
    """Busca dentro de la lista bidimensional `pacientes` por el elemento [0]"""
    busqueda_nhc = int(input("Ingrese el numero de historia clinica: "))
    for paciente in pacientes:
        if paciente[0] == busqueda_nhc:
            print(f"Se ha encontrado al paciente numero {busqueda_nhc}")
            return paciente
    print("Paciente no encontrado.")

def ordenar_pacientes_por_nhc() -> str:
    """Se ordena de manera ascendente la lista bidimensional `pacientes` a traves del algoritmo Bubble Sort y se lo retorna usando un bucle for"""
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                aux = pacientes[j+1]
                pacientes[j + 1] = pacientes[j]
                pacientes[j] = aux    
    for paciente in pacientes:
        print(f"Paciente Numero: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias de internacion: {paciente[4]}")

def paciente_mas_dias_internacion() -> str:
    """Se obtiene a traves de un bucle for que recorre `pacientes` el elemento [4] con mayor valor"""
    max_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > max_paciente[4]:
            max_paciente = paciente
    print(f"El paciente con mas dias de internacion es: {max_paciente[1]} con {max_paciente[4]} dias de internacion")

def paciente_menos_dias_internacion() -> str:
    """Se obtiene a traves de un bucle for que recorre `pacientes` el elemento [4] con menor valor"""
    min_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < min_paciente[4]:
            min_paciente = paciente
    print(f"El paciente con menos dias de internacion es: {min_paciente[1]} con {min_paciente[4]} dias de internacion")

def pacientes_mas_cinco_dias_internacion() -> str:
    """A traves de un bucle for que recorre `pacientes` se obtiene la cantidad de elementos [4] con valor mayor a 5"""
    mas_cinco_dias = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            mas_cinco_dias += 1
    if mas_cinco_dias == 0:
        print("No se han encontrado pacientes con mas de 5 dias de internacion")
    else:
        print(f"Pacientes con mas de 5 dias de internacion: {mas_cinco_dias}")

def pacientes_promedio_dias_internacion() -> str:
    """Se obtiene el promedio de los elementos [4] a traves de un bucle for que recorre `pacientes`"""
    promedio_dias_internacion = 0
    contador_dias_internacion = 0
    for paciente in pacientes:
        promedio_dias_internacion += paciente[4]
        contador_dias_internacion += 1
    promedio_final = promedio_dias_internacion / contador_dias_internacion
    print(f"El promedio de dias de internacion es: {promedio_final}")


def menu_principal():
    """Menu principal del programa. Permite acceder a las distintas funciones"""
    salir = ""
    pacientes_vacio_msj = "No hay pacientes registrados para la operacion solicitada"
    while salir != "s":
        print("""Sistema de Gestion de Clinica
              1. Cargar pacientes
              2. Mostrar todos los pacientes
              3. Buscar pacientes por numero de Historia Clinica
              4. Ordenar pacientes por numero de historia clinica
              5. Mostrar paciente con mas dias de internacion
              6. Mostrar paciente con menos dias de internacion
              7. Cantidad de pacientes con mas de 5 dias de internacion
              8. Promedio de dias de internacion de todos los pacientes
              9. Salir""")
        elegir = int(input("Opcion: "))
        if elegir == 1:
            cantidad_pacientes = int(input("Cuantos pacientes desea ingresar?: "))
            cargar_pacientes(cantidad_pacientes)
        elif elegir == 2:
            if not pacientes:
                print(pacientes_vacio_msj)
            else:
                mostrar_pacientes()
        elif elegir == 3:
            if not pacientes:
                print(pacientes_vacio_msj)
            else:
                print(buscar_pacientes_nhc())
        elif elegir == 4:
            if not pacientes:
                print(pacientes_vacio_msj)
            else:
                ordenar_pacientes_por_nhc()
        elif elegir == 5:
            if not pacientes:
                print(pacientes_vacio_msj)
            else:
                paciente_mas_dias_internacion()
        elif elegir == 6:
            if not pacientes:
                print(pacientes_vacio_msj)
            else:
                paciente_menos_dias_internacion()
        elif elegir == 7:
            if not pacientes:
                print(pacientes_vacio_msj)
            else:
                pacientes_mas_cinco_dias_internacion()
        elif elegir == 8:
            if not pacientes:
                print(pacientes_vacio_msj)
            else:
                pacientes_promedio_dias_internacion()
        elif elegir == 9:
            print("Adiosito!")
            salir = "s"



menu_principal()