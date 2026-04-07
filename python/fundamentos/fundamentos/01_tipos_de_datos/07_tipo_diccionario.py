#Diccionarios en Python
estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
#Imprimir nombre de estudiante
print(estudiante["nombre"]) #Imprime: Gonzalo

#Otro nombre de estudiante
estudiante["nombre"] = "Vicente"
#Imprimir nombre de estudiante
print(estudiante["nombre"]) #Imprime: Vicente

estudiante["nombre"] = "Daniel"
#Imprimir nombre de estudiante
print(estudiante["nombre"]) #Imprime tu nombre: Daniel

paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Peru"
paises["ARG"] = "Argentina"
paises["BOL"] = "Bolivia"
print(paises)

#Paises
if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
    print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
    paises["CRI"] = "Costa Rica"

#Eliminar valores del diccionario
valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
print(f"Valor removido: {valor_removido}")
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

#Diccionario pintor
pintor = {
    "nombre": "Frida Kahlo",
    "pais": "México",
    "fecha_nacimiento": "6 de julio de 1907"
}

#Diccionario anidado
escuela = {
    "nombre": "Coding Dojo LATAM",
    "profesores": [
        {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
        {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
        {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
    ]
}