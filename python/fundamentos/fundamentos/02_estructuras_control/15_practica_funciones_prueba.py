# Ejercicios a desarrollar
# Ejercicio 1
# Crear una función que reciba una lista de números enteros y muestre cuál es el 
# número mayor y cuál es el menor.
def numeroMayorMenor(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El numero mayor es {mayor}\nEl numero menor es: {menor}")

def ejercicio1():
    limit = int(input("Ingresa un limite de valores: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = int(input("Ingresa un numero entero: "))
        listadoNum.append(num)
        i+=1
        numeroMayorMenor(listadoNum)
        pass
    
# Ejercicio 2
# Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales

def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if es_vocal(letra):
            contador += 1
    print(f"La cadena contiene {contador} vocales. ")

def ejercicio_contar_vocales():
    texto = input("Ingrese el texto: ")
    contar_vocales(texto)
ejercicio_contar_vocales()
pass

# Ejercicio 3
# Crear una función que reciba una lista de nombres y muestre únicamente aquellos que 
# tengan más de 5 letras.
def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado

def mostrar():
    nombres = []
    cantidad = int(input("¿Cuántos nombres quieres ingresar? "))
    for i in range(cantidad):
        nombre = input("Ingresa un nombre: ")
        print(f"{nombre} agregado con exito a la lista.")
        nombres.append(nombre)
    for nombre in filtrar(nombres):
        print("Los nombres con más de 5 letras son: ")
        print(nombre)
mostrar()


# Ejercicio 4
# Crear una función que reciba una lista de notas 
# (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
#def listaNotas(notas):
#   lista = 0
#  for i  in range(len(notas)):
#     lista += notas[i]
#    if notas[i] >= 4.0 and notas[i] <= 7.0:
#       print(f"El estudiante {i + 1} pasa con un {notas[i]}")
#  elif



# Ejercicio 5
# Crear una función que reciba una lista de precios de 
# productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * 0.1
    precioFinal = precioInicial - descuento
    print(f"El precio inicial del producto es: \n{precioInicial} y con descuento \n{precioFinal}")

def valores():
    cantidadProductos = int(input("Ingrese la cantidad de productos que quiera:\n "))
    listaPrecios = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Ingrese el valor del producto:\n"))
        listaPrecios.append(valorProducto)
        descuento(listaPrecios)
valores()

# Ejercicio 6
# Crear una función que reciba un número entero y determine si es par o impar.
def parImpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es Par")
    elif numero % 3 == 0:
        print(f"El numero {numero} es Impar")
    else:
        print("Error")

def recibirNum():
    num = int(input("Ingrese un numero: "))
    parImpar(num)
    recibirNum()

# Ejercicio 7
# Crear una función que reciba una lista de edades y muestre cuántas personas son 
# mayores de edad (18 años o más).
def listaEdad(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            num += 1
            return num     
def personas():
    edad = []
    inp = int(input("Cuantas personas vasa ingresar hoy?: "))
    for i in range(inp):
        var = int(input(">> "))
        if var != "":
            edad.append(var)
        else:
            print("Por favor ingresar valor válido")
    resultado = listaEdad(edad)
    print(f"")

            
        



# Ejercicio 8
# Crear una función que reciba una lista de palabras y permita buscar cuántas veces 
# aparece una palabra específica ingresada por el usuario.
def vecesqAparece(palabras):
    buscar = input("Ingrese la palabra que desea buscar: ")
    becesqAparece = 0
    for i in range(len(palabras)):
        if buscar == palabras[i]:
            vecesqAparece += 1
    print(f"La palabra {buscar} aparece {vecesqAparece} en la lista. ")

def recibirpalabras():
    cantidad = int(input("Ingrese la cantidad de palabras"))
    listaPalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}. ")
        listaPalabras.append(palabra)
    vecesqAparece(listaPalabras)

# Ejercicio 9
# Crear una función que reciba una lista de números y genere una nueva lista que contenga
#  únicamente los números positivos.



# Ejercicio 10
# Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.




#Su trabajo debe cumplir con lo siguiente:
#Uso de funciones con parámetros
#Uso de menú con ciclo while
#Uso de input() para solicitar datos
#Uso de listas (arreglos)
#Uso de diccionarios
#Uso de ciclos for
#Uso de estructuras condicionales (if, elif, else)
#Código ordenado, comentado y correctamente indentado
#Opción de salida del programa (0. Salir)
#Menu while
#Menu while
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular mayor y menor")
        print("2. Contar vocales")
        print("3. Filtrar nombres con más de 5 letras")
        print("4. Calcular promedio de notas")
        print("5. Aplicar descuento a precios")
        print("6. Determinar si un número es par o impar")
        print("7. Contar personas mayores de edad")
        print("8. Contar ocurrencias de una palabra")
        print("9. Filtrar números positivos")
        print("10. Mostrar productos con bajo stock")
        print("11. Salir")

        opcion = input("Seleccione una opción (1-11): ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio_contar_vocales()
        elif opcion == "3":
            mostrar()
        elif opcion == "5":
            valores()
            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "6":
            recibirNum()
            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "7":
            personas()
            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "8":

            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "9":

            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "10":

            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "11":

            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

menu()