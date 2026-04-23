# Ejercicio 1
# Ranking de puntajes de un torneo de eSports
puntajesP = [ [1000, 1500, 2000], [300, 700, 1400] ]


puntajesP[1][0] = 600
print(puntajesP) 

# Ejercicio 2
# Lista de creadores de contenido en una plataforma de streaming
nombreStreamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]

nombreStreamers[0]["nombre"] = "EliteGamerX"
print(nombreStreamers)

# Ejercicio 3
# Eventos en distintas ciudades del mundo
paisEventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}

paisEventos["Estados Unidos"][2] = "San Francisco"
print(paisEventos)


#Ejercicio 4
# Coordenadas de la sede de un torneo internacional
coordenada = [
    {"latitud": 34.052235, "longitud": -118.243683}
]

coordenada[0]["latitud"] = "40.712776"
print(coordenada)

# Ejercicio 5
def i_diccionario(lista):
    for i in lista:
        print(f"nombre - {i ['nombre']}, seguidores - {i['seguidores']}")
    
i_diccionario(nombreStreamers)

recibir_valores = {
    "nombre": [
        "EliteGamerX",
        "PixelWarrior",
    ],
    "seguidores": [
        "250000",
        "180000",
    ]
}
def itar_diccionario(Rvalores):
    for tipeclave, lista in Rvalores.items():
        print(f"{len(lista)} {tipeclave.upper()}")
        for element in lista:
            print(element)
        print()    
itar_diccionario(recibir_valores) 

# Ejercicio 6
seccion_lista = {
    "juegos_populares": [
        "Fortnite", 
        "Minecraft", 
        "Valorant", 
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}
def itar_diccionario(Ndiccionario):
    for nclave, list in Ndiccionario.items():
        print(f"{len(list)} {nclave.upper()}")
        for element in list:
            print(element)
        print()    
itar_diccionario(seccion_lista) 



