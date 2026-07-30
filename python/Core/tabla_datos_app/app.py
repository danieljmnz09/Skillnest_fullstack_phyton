from flask import Flask, render_template, request

app = Flask(__name__)

# Tu base de datos original intacta
datos = [
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU."},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU."},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU."},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU."},
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU."},
]


def parse_usuarios(val):
    val = str(val).upper()
    if "B" in val:
        return float(val.replace("B", "")) * 1000
    elif "M" in val:
        return float(val.replace("M", ""))
    return 0


@app.route("/tabla")
def inicio():
    pais_filtro = request.args.get("pais", "todos")
    ordenar_por = request.args.get("ordenar", "nombre")
    direccion = request.args.get("direccion", "asc")

    resultado = datos.copy()

    # 1. Filtro por País
    if pais_filtro != "todos":
        resultado = [p for p in resultado if p["pais"] == pais_filtro]

    # 2. Ordenamiento
    reverse = direccion == "desc"

    if ordenar_por == "nombre":
        resultado.sort(key=lambda x: x["nombre"].lower(), reverse=reverse)
    elif ordenar_por == "usuarios":
        resultado.sort(
            key=lambda x: parse_usuarios(x["usuarios"]), reverse=reverse
        )
    elif ordenar_por == "fundado":
        resultado.sort(key=lambda x: int(x["fundado"]), reverse=reverse)
    elif ordenar_por == "pais":
        resultado.sort(key=lambda x: x["pais"].lower(), reverse=reverse)

    paises_disponibles = sorted(list(set(p["pais"] for p in datos)))

    return render_template(
        "tabla.html",
        plataformas=resultado,
        paises=paises_disponibles,
        pais_sel=pais_filtro,
        orden_sel=ordenar_por,
        dir_sel=direccion,
        total=len(resultado),
    )


if __name__ == "__main__":
    app.run(debug=True)