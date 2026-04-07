""" Imprime en pantalla el texto Hola, mundo usando una sola línea de código."""
print("Hola Mundo")



"""
- Declara una variable nombre con tu nombre o apodo.
- Imprime la frase Hola, <tu nombre> de dos maneras distintas. Por una parte, usando la concatenación con comas y por otra la concatenación con el símbolo +.
- Ejecuta el archivo después de cada forma de concatenación para confirmar que funciona.
"""
nombre = "Daniel"
print("Hola " + nombre)
print("Hola", nombre)



"""
- Declara una variable numero con tu número de la suerte.
- Imprime la frase Mi número de la suerte es el <numero>! de dos maneras distintas. Por una parte, usando la concatenación con comas y por otra la concatenación con el símbolo +.
- Observa que la segunda forma podría lanzar un error si intentas sumar un número con una cadena. Resuélvelo utilizando la conversión de tipo (por ejemplo: str(numero)).
"""
numCuea = str(11)
print("Mi número de la cuea es el",numCuea)
print("Mi número de la cuea es el " + numCuea)



"""
- Declara dos variables llamadas comida1 y comida2 que representen tus comidas favoritas.
- Imprime la frase ¡Me encanta comer <comida1> y <comida2>! de dos maneras distintas. Por una parte, usando format() y por otra usando f-strings.
"""
comida1 = "Pasta con carne molida"
comida2 = "Sopa de pollo"
print("¡Me encanta comer {} y {}!".format(comida1, comida2))
print(f"¡Me encanta comer {comida1} y {comida2}!")