from flask import Flask, request, render_template, redirect, url_for, session
from database import db
from utils import validations as va
from utils import getFromDB
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["MAX_CONTENT_LENGHT"] = 16*1000*1000

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
    errores = session.pop("error_agregar_hincha") if "error_agregar_hincha" in session else None
    regiones, comunas = getFromDB.regiones_comunas()
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
    regiones, comunas = getFromDB.regiones_comunas()
    artesanias = getFromDB.artesanias()
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
    files = request.files.getlist("files")

    errores = va.validate_artesano(region, comuna, artesanias, description, name, email, phone, files)

    if(not errores):
        try:
            id_artesano = db.insert_artesano( comuna, description, name, email, phone)
            for img in files:
                _filename = hashlib.sha256(
                    secure_filename(img.filename).encode("utf-8")
                    ).hexdigest()
                _extension = filetype.guess(img).extension
                img_filename = f"{_filename}.{_extension}"
                img.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                db.insert_foto(app.config["UPLOAD_FOLDER"], img_filename, id_artesano)
            for artesania in artesanias:
                db.insert_artesano_tipo(id_artesano, artesania)
            return render_template("agregar/submit/submited-artesano.html")
        except:
            session["error_agregar_artesano"] = ["error al agregar artesano"]
            return redirect(url_for("registrar_artesano"))
    else:
        session["error_agregar_artesano"] = errores
        return redirect(url_for("registrar_artesano"))



""" Informacion Hinchas """
@app.route("/ver/hinchas")
def ver_hinchas():
    return render_template("ver-hinchas.html")

@app.route("/info/hincha/")
def info_hincha():
    return render_template("informacion-hincha.html")

""" Informacion Artesanos"""
@app.route("/ver/artesanos/<int:page>")
def ver_artesanos(page):
    if page < 0:
        return redirect(url_for("ver_artesanos", page=0))
    maxPage = (db.get_artesanos_total()[0]-1)//5
    if page > maxPage:
        return redirect(url_for("ver_artesanos", page=maxPage))
    artesanos = getFromDB.artesanos(offset=page*5)

    page_info = {"current":page,"max":maxPage}
    return render_template("ver/ver-artesanos.html", artesanos=artesanos, page=page_info)

@app.route("/info/artesano/<int:id_artesano>")
def info_artesano(id_artesano):
    try:
        artesano = getFromDB.artesano(id_artesano)
        return render_template("info/informacion-artesano.html", artesano=artesano)
    except:
        return redirect(url_for("ver_artesanos", page=0))





def error_404(error):
    return redirect(url_for("index"))
app.register_error_handler(404, error_404)

if __name__ == "__main__":
    app.run(debug=True)