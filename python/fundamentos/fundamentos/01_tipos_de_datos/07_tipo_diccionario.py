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


