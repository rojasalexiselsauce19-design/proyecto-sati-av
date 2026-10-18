from flask import Flask, render_template, request, redirect, url_for, flash
from data.db import guardar_solicitud_desbloqueo 


app = Flask(__name__, template_folder='presentation/templates', static_folder='presentation/static')
app.secret_key = "clave_secreta" 

PASSWORD = "1999"  

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    password = request.form["password"]
    if password == PASSWORD:
        return redirect(url_for("formulario"))
    else:
        flash("❌ Contraseña incorrecta", "error")
        return redirect(url_for("login_page"))

@app.route("/formulario")
def formulario():
    return render_template("index.html")

@app.route("/guardar", methods=["POST"])
def guardar():
    carnet = request.form["carnet"]
    carrera = request.form["carrera"]
    motivo = request.form["motivo"]

    mensaje = guardar_solicitud_desbloqueo(carnet, carrera, motivo)

    if "Error" in mensaje:
        flash(mensaje, "error")
    else:
        flash(mensaje, "success")

    return redirect(url_for("formulario"))

if __name__ == "__main__":
    app.run(debug=True)
