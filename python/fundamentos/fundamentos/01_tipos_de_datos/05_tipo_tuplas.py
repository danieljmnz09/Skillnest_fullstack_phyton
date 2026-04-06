#Tuplas ejemplos
tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"

#Cualquier tipo de dato ejemplo: 
gato = ("Miu", 5, "persa", False)

print(gato[0]) #Imprime: Miu

#Ejemplo de error en tuplas
#gato[0] = "Michi" #ERROR: TypeError: 'tuple' object does not support item assignment

gato = gato + ("4.1",)
print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')

#Tuplas dentro de funciones
def suma_multiplicacion(x, y):
    suma = x + y
    multiplicacion = x * y
    return (suma, multiplicacion(10, 5))

print(suma_multiplicacion(10, 5))