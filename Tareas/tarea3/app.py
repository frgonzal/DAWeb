from flask import Flask, request, render_template, redirect, url_for, session, jsonify

from database import db
from utils import validations as va
from utils import getFromDB

from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
import uuid

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

Transportes_disponibles = ["Particular", "Locomoción pública"]

## To read the secret key
with open("./secret/secretkey.txt", "r") as keyFile:
    app.secret_key = keyFile.read()


""" Pagina de inicio """
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


##########################
###  Registro Hinchas  ###
##########################
@app.route("/registrar/hincha", methods=["GET"])
def registrar_hincha():
    errores = session.pop("err_hincha") if "err_hincha" in session else None
    transportes = Transportes_disponibles
    regiones, comunas = getFromDB.regiones_comunas()
    sports = db.get_sports()
    return render_template("agregar/agregar-hincha.html", errores=errores, regiones=regiones, comunas=comunas, sports=sports, transportes=transportes)

@app.route("/registrar/submited-hincha", methods=["POST"])
def submited_hincha():
    form   = request.form
    sports = form.getlist("sports[]")
    region = form.get("regiones")
    comuna = form.get("comunas")
    transp = form.get("transporte")
    name   = form.get("name")
    email  = form.get("email")
    phone  = form.get("phone")
    comment = form.get("comentarios")
    errores = va.validate_hincha(sports, region, comuna, transp, name, email, phone, comment)
    if(not errores):
        try:
            id_hincha = db.insert_hincha(comuna, transp, name, email, phone, comment)
            for sport in sports:
                db.insert_hincha_deporte(id_hincha, sport)
            return render_template("agregar/submit/submited-hincha.html")
        except:
            session["err_hincha"] = ["error al agregar hincha"]
            return redirect(url_for("registrar_hincha"))
    else:
        session["err_hincha"] = errores
        return redirect(url_for("registrar_hincha"))


###########################
###  Registro Artesano  ###
###########################
@app.route("/registrar/artesano", methods=["GET"])
def registrar_artesano():
    errores = session.pop("err_artesano") if "err_artesano" in session else None
    regiones, comunas = getFromDB.regiones_comunas()
    artesanias = db.get_artesanias()
    return render_template("agregar/agregar-artesano.html", errores=errores, regiones=regiones, comunas=comunas, artesanias=artesanias)

@app.route("/registrar/submited-artesano", methods=["POST"])
def submited_artesano():
    form   = request.form
    region = form.get("regiones")
    comuna = form.get("comunas")
    artesanias  = form.getlist("crafts[]")
    description = form.get("description")
    name  = form.get("name")
    email = form.get("email")
    phone = form.get("phone")
    files = request.files.getlist("files[]")

    errores = va.validate_artesano(region, comuna, artesanias, description, name, email, phone, files)

    if(not errores):
        try:
            id_artesano = db.insert_artesano( comuna, description, name, email, phone)

            for img in files:
                _filename = hashlib.sha256(
                        secure_filename(img.filename).
                        encode("utf-8")
                    ).hexdigest()
                _extension = filetype.guess(img).extension
                img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"
                img.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                db.insert_foto(app.config["UPLOAD_FOLDER"], img_filename, id_artesano)

            for artesania in artesanias:
                db.insert_artesano_tipo(id_artesano, artesania)
            return render_template("agregar/submit/submited-artesano.html")
        except:
            session["err_artesano"] = ["error al agregar artesano"]
            return redirect(url_for("registrar_artesano"))

    else:
        session["err_artesano"] = errores
        return redirect(url_for("registrar_artesano"))


###########################
### Informacion Hinchas ###
###########################
@app.route("/ver/hinchas/<int:page>")
def ver_hinchas(page):
    maxPage = (db.get_total_tabla("hincha")-1)//5
    if page > maxPage:
        return redirect(url_for("ver_hinchas", page=maxPage))
    hinchas = getFromDB.hinchas(offset=page*5)
    page_info = {"current":page,"max":maxPage}
    return render_template("ver/ver-hinchas.html", hinchas=hinchas, page_info=page_info)

@app.route("/info/hincha/<int:id_hincha>")
def info_hincha(id_hincha):
    try:
        hincha = getFromDB.hincha(id_hincha)
    except:
        hincha = None
    return render_template("info/informacion-hincha.html", hincha=hincha)

#############################
### Informacion Artesanos ###
#############################
@app.route("/ver/artesanos/<int:page>")
def ver_artesanos(page):
    maxPage = (db.get_total_tabla("artesano")-1)//5
    if page > maxPage:
        return redirect(url_for("ver_artesanos", page=maxPage))
    artesanos = getFromDB.artesanos(offset=page*5)
    page_info = {"current":page,"max":maxPage}
    return render_template("ver/ver-artesanos.html", artesanos=artesanos, page_info=page_info)

@app.route("/info/artesano/<int:id_artesano>")
def info_artesano(id_artesano):
    try:
        artesano = getFromDB.artesano(id_artesano)
    except:
        artesano = None
    return render_template("info/informacion-artesano.html", artesano=artesano)



###############################
#####    Estadísticas     #####
###############################
@app.route("/estadisticas/ver", methods=["GET"])
def estadisticas():
    return render_template("estadisticas.html")

@app.route("/estadisticas/informacion_hinchas", methods=["GET"])
def grafico_hinchas():
    categories = []
    data = []
    for sport, count in db.count_hinchas_by_sport():
        categories.append(sport)
        data.append(count)
    data = {"categories":categories, "data":data}
    return jsonify({"status": "ok", "data":data})

@app.route("/estadisticas/informacion_artesanos", methods=["GET"])
def grafico_artesanos():
    categories = []
    data = []
    for artesania, count in db.count_artesanos_by_artesania():
        categories.append(artesania)
        data.append(count)
    data = {"categories":categories, "data":data}
    return jsonify({"status": "ok", "data":data})

##########################################
def error_404(error):
    return redirect(url_for("index"))
app.register_error_handler(404, error_404)

if __name__ == "__main__":
    app.run(debug=True)