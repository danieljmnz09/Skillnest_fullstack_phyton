#funciones en Python
def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado

a = int(input("ingrese primer número"))
b = int(input("ingrese segundo número"))
resultado_multiplicacion = multiplicacion(a, b)
#Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion)
#Se guarda en la variable el resultado que la funcion regresó. Imprime: 25

#Parametros y argumentos
def buenos_dias(nombre):
   print("Buenos días " + nombre)
# Llamada a la funcion y asignacion de valor a parámetro

buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")

#Devolucion de valores
def buenos_dias2(nombre):
   return "Buenos días "+nombre

#El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese

frase = buenos_dias2("Python")
print(frase) #Imprime: Buenos días Python

#Ejercicio de retorno de valor 
#Crear una funcion que reciba una frase + un parametro 
#Devolver el valor de la frase completa e imprimir

def devolver_frase(frase, palabra):
   print(f"{frase} \n {palabra}")
   devolver_frase("Que tipo de deporte prefieres?")