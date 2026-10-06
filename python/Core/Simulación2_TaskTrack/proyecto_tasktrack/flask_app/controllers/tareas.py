from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.tarea import Tarea
from flask_app.models.categoria import Categoria

@app.route("/tareas")
def dashboard_tareas():
    if "usuario_id" not in session:
        return redirect("/")

    tareas = Tarea.get_all_by_user(session["usuario_id"])

    # Cálculos dinámicos para la sección Resumen
    total_tareas = len(tareas)
    pendientes = sum(1 for t in tareas if t.estado == "Pendiente")
    en_progreso = sum(1 for t in tareas if t.estado == "En progreso")
    completadas = sum(1 for t in tareas if t.estado == "Completada")

    resumen = {
        "total": total_tareas,
        "pendientes": pendientes,
        "en_progreso": en_progreso,
        "completadas": completadas
    }

    # Próximas tareas (las 3 más cercanas)
    proximas = [t for t in tareas if t.estado != "Completada"][:3]

    return render_template("dashboard.html", tareas=tareas, resumen=resumen, proximas=proximas)

@app.route("/tareas/nueva")
def formulario_nueva_tarea():
    if "usuario_id" not in session:
        return redirect("/")

    categorias = Categoria.get_all_by_user(session["usuario_id"])
    return render_template("nueva_tarea.html", categorias=categorias)

@app.route("/tareas/crear", methods=["POST"])
def crear_tarea():
    if "usuario_id" not in session:
        return redirect("/")

    if not Tarea.validar_tarea(request.form):
        return redirect("/tareas/nueva")

    datos = {
        "titulo": request.form["titulo"],
        "descripcion": request.form["descripcion"],
        "prioridad": request.form["prioridad"],
        "fecha_limite": request.form["fecha_limite"],
        "categoria_id": request.form["categoria_id"],
        "usuario_id": session["usuario_id"]
    }
    Tarea.save(datos)
    return redirect("/tareas")

@app.route("/tareas/<int:id>")
def ver_detalle_tarea(id):
    if "usuario_id" not in session:
        return redirect("/")

    tarea = Tarea.get_by_id(id)
    # Verificación de permisos
    if not tarea or tarea.usuario_id != session["usuario_id"]:
        return redirect("/tareas")

    return render_template("detalle_tarea.html", tarea=tarea)

@app.route("/tareas/editar/<int:id>")
def formulario_editar_tarea(id):
    if "usuario_id" not in session:
        return redirect("/")

    tarea = Tarea.get_by_id(id)
    if not tarea or tarea.usuario_id != session["usuario_id"]:
        return redirect("/tareas")

    categorias = Categoria.get_all_by_user(session["usuario_id"])
    return render_template("editar_tarea.html", tarea=tarea, categorias=categorias)

@app.route("/tareas/<int:id>/actualizar", methods=["POST"])
def actualizar_tarea(id):
    if "usuario_id" not in session:
        return redirect("/")

    if not Tarea.validar_tarea(request.form):
        return redirect(f"/tareas/editar/{id}")

    datos = {
        "id": id,
        "titulo": request.form["titulo"],
        "descripcion": request.form["descripcion"],
        "prioridad": request.form["prioridad"],
        "fecha_limite": request.form["fecha_limite"],
        "categoria_id": request.form["categoria_id"],
        "usuario_id": session["usuario_id"]
    }
    Tarea.update(datos)
    return redirect("/tareas")

@app.route("/tareas/<int:id>/completar", methods=["POST"])
def completar_tarea(id):
    if "usuario_id" not in session:
        return redirect("/")

    datos = {"id": id, "estado": "Completada", "usuario_id": session["usuario_id"]}
    Tarea.update_estado(datos)
    return redirect(f"/tareas/{id}")

@app.route("/tareas/<int:id>/borrar", methods=["POST"])
def borrar_tarea(id):
    if "usuario_id" not in session:
        return redirect("/")

    datos = {"id": id, "usuario_id": session["usuario_id"]}
    Tarea.delete(datos)
    return redirect("/tareas")