from flask import Flask, request, render_template, redirect, url_for
from database import db
from utils import validations as va

app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/registrar-hincha")
def registrar_hincha():
    return render_template("agregar-hincha.html")

@app.route("/registrar-artesano/", methods=["GET", "POST"])
def registrar_artesano():
    error = []
    if request.method == "POST":
        if(va.validate_artesano(request.form) and va.validate_files(request.files.get("files"))):
            ## post artesano...
            return redirect(url_for("index"))
        else:
            error = "Error: ..."

    regiones = []
    comunas  = {}
    for region in db.get_regiones():
        id_region, nombreRegion = region
        regiones.append(nombreRegion)
        listaComunas = []
        for comuna in db.get_comunas_by_region(id_region):
            _, nombreComuna = comuna
            listaComunas.append(nombreComuna)
        comunas[nombreRegion] = listaComunas
    artesanias = []
    for art in db.get_artesanias():
        _, artesania = art
        artesanias.append(artesania)
    return render_template("agregar-artesano.html", error=error, regiones=regiones, comunas=comunas, artesanias=artesanias)









@app.route("/ver-hinchas/")
def ver_hinchas():
    return render_template("ver-hinchas.html")

@app.route("/ver-artesanos/")
def ver_artesanos():
    return render_template("ver-artesanos.html")

@app.route("/info-hincha/")
def info_hincha():
    return render_template("informacion-hincha.html")

@app.route("/info-artesano/")
def info_artesano():
    return render_template("informacion-artesano.html")



if __name__ == "__main__":
    app.run(debug=True)