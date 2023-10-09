from flask import Flask, request, render_template, redirect, url_for, session
from database import db
from utils import validations as va
from utils import toList

app = Flask(__name__)

## To read the secret key
with open("./utils/secretkey.txt", "r") as keyFile:
    app.secret_key = str(keyFile.read())


""" Pagina de inicio """
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")



""" Registro de un hincha """
@app.route("/registrar/hincha", methods=["GET"])
def registrar_hincha():
    if "error_agregar_hincha" in session:
        errores = session.pop("error_agregar_hincha")
    else:
        errores = None
    regiones, comunas = toList.regiones_comunas()
    return render_template("agregar/agregar-hincha.html", errores=errores, regiones=regiones, comunas=comunas)

@app.route("/registrar/submited-hincha", methods=["POST"])
def submited_hincha():
    return render_template("agregar/submit/submited-hincha.html")



""" Registro de un Artesano """
@app.route("/registrar/artesano", methods=["GET"])
def registrar_artesano():
    if "error_agregar_artesano" in session:
        errores = session.pop("error_agregar_artesano")
    else:
        errores = None
    regiones, comunas = toList.regiones_comunas()
    artesanias = toList.artesanias()
    return render_template("agregar/agregar-artesano.html", errores=errores, regiones=regiones, comunas=comunas, artesanias=artesanias)

@app.route("/registrar/submited-artesano", methods=["POST"])
def submited_artesano():
    errores = va.validate_artesano(request)

    if(not errores):
        ## post artesano...
        return render_template("agregar/submit/submited-artesano.html")
    else:
        session["error_agregar_artesano"] = errores
        return redirect(url_for("registrar_artesano"))



@app.route("/ver/hinchas")
def ver_hinchas():
    return render_template("ver-hinchas.html")

@app.route("/ver/artesanos")
def ver_artesanos():
    return render_template("ver-artesanos.html")

@app.route("/info/hincha/")
def info_hincha():
    return render_template("informacion-hincha.html")

@app.route("/info/artesano/")
def info_artesano():
    return render_template("informacion-artesano.html")


if __name__ == "__main__":
    app.run(debug=True)