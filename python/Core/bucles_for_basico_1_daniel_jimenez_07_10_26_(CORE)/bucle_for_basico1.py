import sys

def ejercicio_1():
    print("\n--- Ejercicio 1: Generador de niveles ---")
    for nivel in range(101):
        print(nivel, end=" ")  # Imprime al lado con espacio para no saturar la pantalla
    print()

def ejercicio_2():
    print("\n--- Ejercicio 2: Potenciadores de energía ---")
    for posicion in range(2, 501, 2):
        print(posicion, end=", " if posicion < 500 else "")
    print()

def ejercicio_3():
    print("\n--- Ejercicio 3: Trampa de emojis ---")
    for punto in range(1, 101):
        if punto % 10 == 0:
            print("🤖", end=" ")
        elif punto % 5 == 0:
            print("👾", end=" ")
        else:
            print(punto, end=" ")
    print()

def ejercicio_4():
    print("\n--- Ejercicio 4: Suma colosal ---")
    suma_total = 0
    for segundo in range(0, 500001, 2):
        suma_total += segundo
    print(f"El total acumulado de experiencia es: {suma_total}")

def ejercicio_5():
    print("\n--- Ejercicio 5: Retroceso temporal ---")
    for anio in range(2024, -1, -3):
        print(anio, end=" ")
    print()

def ejercicio_6():
    print("\n--- Ejercicio 6: Contador dinámico ---")
    inicio = 3
    fin = 10
    salto = 2
    
    print(f"Configuración: inicio={inicio}, fin={fin}, salto={salto}")
    print("Múltiplos encontrados:")
    for numero in range(inicio, fin + 1):
        if numero % salto == 0:
            print(numero, end=" ")
    print()

def menu():
    while True:
        print("\n" + "="*40)
        print("    MENÚ PRINCIPAL - BUCLES FOR 1    ")
        print("="*40)
        print("1. Generador de niveles (0 al 100)")
        print("2. Potenciadores de energía (2 al 500)")
        print("3. Trampa de emojis (1 al 100)")
        print("4. Suma colosal (Bonus de experiencia)")
        print("5. Retroceso temporal (2024 a 0)")
        print("6. Contador dinámico")
        print("7. Salir")
        print("="*40)
        
        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("\n⚠️ Opción no válida. Por favor, ingresa un número del 1 al 7.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu()