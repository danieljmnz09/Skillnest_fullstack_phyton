# Mini Core
Ndatos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]

for Npersona in Ndatos:
    if Npersona["nombre"] == "Pedro":
        Npersona["puntaje"] = 75

def mostrar_mensajes(lista):
    for persona in lista:
        print(f"{persona["nombre"]} obtuvo {persona["puntaje"]} puntos")

def mostrar_campo(lista, campo):
    for persona in lista:
        if campo in persona:
            print(persona[campo])
        else:
            print("Campo no válido")

mostrar_mensajes(Ndatos)
print("-----")
mostrar_campo(Ndatos, "nombre")
print("-----")
mostrar_campo(Ndatos, "puntaje")

