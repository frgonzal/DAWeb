from flask import Flask, request, render_template, redirect, url_for




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
    return render_template("agregar-artesano.html")

@app.route("/ver_hinchas")
def ver_hinchas():
    return render_template("ver-hinchas.html")

@app.route("/ver_artesanos")
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