# Lista principal de Estudiantes

estudiantes = []



# Función para mostrar el menu

def mostrar_menu():

    print("\n========== MENÚ PRINCIPAL ==========")

    print("1. Agregar estudiante")

    print("2. Buscar estudiante")

    print("3. Eliminar estudiante")

    print("4. Actualizar estados")

    print("5. Mostrar estudiantes")

    print("6. Salir")

    print("=====================================")

# Funcion para leer opcion valida

def leer_opcion():

    while True:

        try:

            opcion = int(input("Seleccione una opción: "))

            if 1 <= opcion <= 6:

                return opcion

            else:

                print("Debe ingresar una opción entre 1 y 6.")

        except ValueError:

            print("Ingrese un número válido.")

# Validaciones

def validar_nombre(nombre):

    return nombre.strip() != ""

def validar_edad(edad):

    return edad > 0

def validar_nota(nota):

    return 1.0 <= nota <= 7.0

# Agregar estudiante

def agregar_estudiante(lista):

    nombre = input("Ingrese nombre: ")

    try:

        edad = int(input("Ingrese edad: "))

    except ValueError:

        print("Error: La edad debe ser un número entero.")

        return

    try:

        nota = float(input("Ingrese nota: "))

    except ValueError:

        print("Error: La nota debe ser un número decimal.")

        return

    if not validar_nombre(nombre):

        print("Error: El nombre no puede estar vacío.")

        return

    if not validar_edad(edad):

        print("Error: La edad debe ser mayor que cero.")

        return

    if not validar_nota(nota):

        print("Error: La nota debe estar entre 1.0 y 7.0.")

        return

    estudiante = {

        "nombre": nombre,

        "edad": edad,

        "nota": nota,

        "aprobado": False

    }

    lista.append(estudiante)

    print("Estudiante registrado correctamente.")

# Buscar estudiante

def buscar_estudiante(lista, nombre):

    for i in range(len(lista)):

        if lista[i]["nombre"] == nombre:

            return i

    return -1

# Eliminar estudiante

def eliminar_estudiante(lista):

    nombre = input("Ingrese el nombre del estudiante a eliminar: ")

    posicion = buscar_estudiante(lista, nombre)

    if posicion != -1:

        lista.pop(posicion)

        print("Estudiante eliminado correctamente.")

    else:

        print(f"El estudiante '{nombre}' no se encuentra registrado.")

# Actualizar estados

def actualizar_estados(lista):

    for estudiante in lista:

        if estudiante["nota"] >= 4.0:

            estudiante["aprobado"] = True

        else:

            estudiante["aprobado"] = False

# Mostrar estudiantes

def mostrar_estudiantes(lista):

    actualizar_estados(lista)

    print("\n=== LISTA DE ESTUDIANTES ===")

    if len(lista) == 0:

        print("No hay estudiantes registrados.")

        return

    for estudiante in lista:

        estado = "APROBADO"

        if not estudiante["aprobado"]:

            estado = "REPROBADO"

        print(f"Nombre: {estudiante['nombre']}")

        print(f"Edad: {estudiante['edad']}")

        print(f"Nota: {estudiante['nota']}")

        print(f"Estado: {estado}")

        print("*" * 45)

# Programa principal

while True:

    mostrar_menu()

    opcion = leer_opcion()

    if opcion == 1:

        agregar_estudiante(estudiantes)

    elif opcion == 2:

        nombre = input("Ingrese nombre a buscar: ")

        posicion = buscar_estudiante(estudiantes, nombre)

        if posicion != -1:

            print(f"\nPosición encontrada: {posicion}")

            print(estudiantes[posicion])

        else:

            print("Estudiante no encontrado.")

    elif opcion == 3:

        eliminar_estudiante(estudiantes)

    elif opcion == 4:

        actualizar_estados(estudiantes)

        print("Estados actualizados correctamente.")

    elif opcion == 5:

        mostrar_estudiantes(estudiantes)

    elif opcion == 6:

        print("Gracias por usar el sistema. Vuelva Pronto")

        break