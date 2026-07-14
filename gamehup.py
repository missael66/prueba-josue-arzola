

# 1. Diccionarios Iniciales del Sistema


juegos = {

  'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],

  'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],

  'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],

  'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],

  'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],

  'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']

}



inventario = {

  'G001': [9990, 7],

  'G002': [19990, 0],

  'G003': [42990, 3],

  'G004': [14990, 5],

  'G005': [17990, 9],

  'G006': [39990, 2]

}




#=============



def validar_codigo(codigo):

  """Valida que el código no esté vacío y no exista en los diccionarios."""

  if not codigo or codigo.strip() == "":

    return False

  if codigo.strip().upper() in juegos:

    return False

  return True



def validar_titulo(titulo):

  """Valida que el título no esté vacío ni contenga solo espacios."""

  return bool(titulo and titulo.strip())



def validar_plataforma(plataforma):

  """Valida que la plataforma no esté vacía ni contenga solo espacios."""

  return bool(plataforma and plataforma.strip())



def validar_genero(genero):

  """Valida que el género no esté vacío ni contenga solo espacios."""

  return bool(genero and genero.strip())



def validar_clasificacion(clasificacion):

  """Valida que la clasificación sea exactamente 'E', 'T' o 'M'."""

  return clasificacion in ['E', 'T', 'M']



def validar_multiplayer(multiplayer):

  """Valida que la respuesta sea 's' o 'n'."""

  return multiplayer.lower() in ['s', 'n']



def validar_editor(editor):

  """Valida que el editor no esté vacío ni contenga solo espacios."""

  return bool(editor and editor.strip())



def validar_precio(precio_str):

  """Valida que el precio sea un número entero mayor que cero."""

  try:

    precio = int(precio_str)

    return precio > 0

  except ValueError:

    return False



def validar_stock(stock_str):

  """Valida que el stock sea un número entero mayor o igual a cero."""

  try:

    stock = int(stock_str)

    return stock >= 0

  except ValueError:

    return False





#=====================================================================






# --- OPCIÓN 1: Stock por plataforma ---

def stock_plataforma(plataforma):

  total_stock = 0

  plataforma_buscar = plataforma.strip().lower()

   

  for cod, datos in juegos.items():

    if datos[1].lower() == plataforma_buscar:

      if cod in inventario:

        total_stock += inventario[cod][1]

         

  print(f"El total de stock disponibles es: {total_stock}")





# --- OPCIÓN 2: Búsqueda por rango de precio ---

def busqueda_precio(p_min, p_max):

  resultados = []

   

  for cod, datos_inv in inventario.items():

    precio = datos_inv[0]

    stock = datos_inv[1]

     

    if p_min <= precio <= p_max and stock > 0:

      if cod in juegos:

        titulo = juegos[cod][0]

        resultados.append(f"{titulo}--{cod}")

         

  if not resultados:

    print("No hay juegos en ese rango de precios.")

  else:

    resultados.sort()

    print(f"Los juegos encontrados son: {resultados}")





# --- OPCIÓN 3: Actualizar precio ---

def actualizar_precio(codigo, nuevo_precio):

  cod_key = codigo.strip().upper()

  if cod_key in inventario:

    inventario[cod_key][0] = nuevo_precio

    return True

  return False





# --- OPCIÓN 4: Agregar juego ---

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):

  cod_key = codigo.strip().upper()

   

  if cod_key in juegos:

    return False

   

  es_multiplayer = True if multiplayer.lower() == 's' else False

   

  juegos[cod_key] = [titulo.strip(), plataforma.strip(), genero.strip(), clasificacion, es_multiplayer, editor.strip()]

  inventario[cod_key] = [int(precio), int(stock)]

   

  return True





# --- OPCIÓN 5: Eliminar juego ---

def eliminar_juego(codigo):

  cod_key = codigo.strip().upper()

   

  if cod_key in juegos and cod_key in inventario:

    del juegos[cod_key]

    del inventario[cod_key]

    return True

     

  return False


# =====================================================================


def main():

  while True:

    print("\n========== MENÚ PRINCIPAL ==========")

    print("1. Stock por plataforma")

    print("2. Búsqueda de juegos por rango de precio")

    print("3. Actualizar precio de juego")

    print("4. Agregar juego")

    print("5. Eliminar juego")

    print("6. Salir")

    print("=====================================")

     

    opcion = input("Ingrese opción: ").strip()

     

    if opcion == '1':

      plat = input("Ingrese plataforma a consultar: ")

      stock_plataforma(plat)

       

    elif opcion == '2':

      while True:

        try:

          p_min_str = input("Ingrese precio mínimo: ")

          p_min = int(p_min_str)

           

          p_max_str = input("Ingrese precio máximo: ")

          p_max = int(p_max_str)

           

          if p_min >= 0 and p_max >= 0 and p_min <= p_max:

            break

          else:

            print("Debe ingresar valores enteros")

        except ValueError:

          print("Debe ingresar valores enteros")

           

      busqueda_precio(p_min, p_max)

       

    elif opcion == '3':

      while True:

        cod = input("Ingrese código del juego: ")

        nuevo_p_str = input("Ingrese nuevo precio: ")

         

        if validar_precio(nuevo_p_str):

          nuevo_p = int(nuevo_p_str)

          exito = actualizar_precio(cod, nuevo_p)

           

          if exito:

            print("Precio actualizado")

          else:

            print("El código no existe")

        else:

          print("El precio debe ser un número entero mayor a cero.")

         

        repetir = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()

        if repetir != 's':

          break

           

    elif opcion == '4':

      cod = input("Ingrese código del juego: ")

      if not validar_codigo(cod):

        print("El código ya existe o no es válido")

        continue

         

      tit = input("Ingrese título: ")

      if not validar_titulo(tit):

        print("El título no puede estar vacío")

        continue

         

      plat = input("Ingrese plataforma: ")

      if not validar_plataforma(plat):

        print("La plataforma no puede estar vacía")

        continue

         

      gen = input("Ingrese género: ")

      if not validar_genero(gen):

        print("El género no puede estar vacío")

        continue

         

      clas = input("Ingrese clasificación: ")

      if not validar_clasificacion(clas):

        print("La clasificación debe ser 'E', 'T' o 'M'")

        continue

         

      mult = input("¿Es multiplayer? (s/n): ")

      if not validar_multiplayer(mult):

        print("Debe ingresar 's' o 'n'")

        continue

         

      edit = input("Ingrese editor: ")

      if not validar_editor(edit):

        print("El editor no puede estar vacío")

        continue

         

      prec = input("Ingrese precio: ")

      if not validar_precio(prec):

        print("El precio debe ser un entero mayor que cero")

        continue

         

      stk = input("Ingrese stock: ")

      if not validar_stock(stk):

        print("El stock debe ser un entero mayor o igual a cero")

        continue

       

      agregado = agregar_juego(cod, tit, plat, gen, clas, mult, edit, prec, stk)

      if agregado:

        print("Juego agregado")

      else:

        print("El código ya existe")

         

    elif opcion == '5':

      cod = input("Ingrese código del juego: ")

      eliminado = eliminar_juego(cod)

      if eliminado:

        print("Juego eliminado")

      else:

        print("El código no existe")

         

    elif opcion == '6':

      print("Programa finalizado.")

      break

       

    else:

      print("Debe seleccionar una opción válida")



if __name__ == '__main__':

  main()