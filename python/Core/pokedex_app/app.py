from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de Pokémon
pokedex = [
    {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
    {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
    {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
    {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
    {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
    {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
    {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
    {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
    {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
    {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]

# Mostrar todos los Pokémon
@app.route("/pokemon")
def inicio():
    return render_template(
        "pokemon.html",
        pokedex=pokedex, subtitulo="Todos los Pokémon"
    )


# Mostrar Pokémon específico por nombre
@app.route("/pokemon/<nombre>")
def mostrar_pokemon(nombre):

    pokemon_encontrado = []

    for pokemon in pokedex:
        if pokemon["nombre"].lower() == nombre.lower():
            pokemon_encontrado.append(pokemon)

    if pokemon_encontrado:
        return render_template(
            "pokemon.html",
            pokedex=pokemon_encontrado, subtitulo=f"Pokémon: {pokemon_encontrado[0]['nombre']}"
        )

    return pokemon_no_encontrado(
        "El Pokémon que buscas no existe"
    )


# Mostrar un Pokémon por número de Pokédex
@app.route("/pokemon/numero/<int:numero>")
def pokemon_por_numero(numero):

    pokemon_encontrado = []

    for pokemon in pokedex:
        if pokemon["id"] == numero:
            pokemon_encontrado.append(pokemon)

    if pokemon_encontrado:
        return render_template(
            "pokemon.html",
            pokedex=pokemon_encontrado, subtitulo=f"Pokédex #{numero}"
        )

    return pokemon_no_encontrado(
        "No existe un Pokémon con ese número de Pokédex"
    )


# Mostrar los primeros N Pokémon
@app.route("/pokemon/cantidad/<int:cantidad>")
def mostrar_cantidad(cantidad):

    pokemones_mostrados = pokedex[:cantidad]

    return render_template(
        "pokemon.html",
        pokedex=pokemones_mostrados, subtitulo=f"Primeros {cantidad} Pokémon"
    )


# Página de error
def pokemon_no_encontrado(mensaje):
    return render_template(
        "404.html",
        mensaje=mensaje
    )


if __name__ == "__main__":
    app.run(debug=True)