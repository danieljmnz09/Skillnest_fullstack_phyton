from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.categoria import Categoria

@app.route("/categorias")
def listar_categorias():
    if "usuario_id" not in session:
        return redirect("/")
    
    categorias = Categoria.get_all_by_user(session["usuario_id"])
    return render_template("categorias.html", categorias=categorias)

@app.route("/categorias/nueva")
def formulario_nueva_categoria():
    if "usuario_id" not in session:
        return redirect("/")
    
    return render_template("nueva_categoria.html")

@app.route("/categorias/crear", methods=["POST"])
def crear_categoria():
    if "usuario_id" not in session:
        return redirect("/")
    
    usuario_id = session["usuario_id"]

    # Validar el formulario antes de guardar
    if not Categoria.validar_categoria(request.form, usuario_id):
        return redirect("/categorias/nueva")

    # Armar diccionario con datos limpios
    datos = {
        "nombre": request.form["nombre"].strip(),
        "usuario_id": usuario_id
    }
    
    Categoria.save(datos)
    return redirect("/categorias")

@app.route("/categorias/<int:id>/eliminar", methods=["POST"])
def eliminar_categoria(id):
    if "usuario_id" not in session:
        return redirect("/")

    datos = {"id": id, "usuario_id": session["usuario_id"]}
    Categoria.delete(datos)
    return redirect("/categorias")