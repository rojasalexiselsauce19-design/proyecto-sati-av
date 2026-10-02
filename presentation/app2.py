from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    password = request.form["password"]
    if password == "1999":  # contraseña correcta
        return redirect(url_for("formulario"))
    else:
        return "Contraseña incorrecta"

@app.route("/formulario")
def formulario():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
