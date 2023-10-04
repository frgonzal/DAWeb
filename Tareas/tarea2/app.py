from flask import Flask, request, render_template, redirect, url_for
from database import db

app = Flask(__name__)

@app.route("/")
def index_():
    return redirect(url_for('index'))


@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/registrar_hincha/")
def registrar_hincha():
    return render_template("agregar-hincha.html")

@app.route("/registrar_artesano/")
def registrar_artesano():
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
    return render_template("agregar-artesano.html", regiones=regiones, comunas=comunas)

@app.route("/ver_hinchas/")
def ver_hinchas():
    return render_template("ver-hinchas.html")

@app.route("/ver_artesanos/")
def ver_artesanos():
    return render_template("ver-artesanos.html")

@app.route("/info_hincha/")
def info_hincha():
    return render_template("informacion-hincha.html")

@app.route("/info_artesano/")
def info_artesano():
    return render_template("informacion-artesano.html")



if __name__ == "__main__":
    app.run(debug=True)