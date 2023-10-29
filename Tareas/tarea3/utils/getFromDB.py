from database import db
from flask import url_for

def regiones_comunas():
    regiones = []
    comunas  = {}
    for id_region, nombreRegion in db.get_regiones():
        regiones.append(nombreRegion)
        listaComunas = db.get_comunas_by_region(id_region)
        comunas[nombreRegion] = listaComunas
    return regiones, comunas


def artesanos(offset):
    artesanos = []
    artesanos_ = db.get_artesanos(offset)

    for artesano_ in artesanos_:
        artesano = {}

        id_artesano, name, phone, comuna = artesano_

        artesanias = db.get_artesanias_by_id_artesano(id_artesano)
        ruta_file, filename  = db.get_file_by_id_artesano(id_artesano)
        ruta_file = ruta_file.replace("static/","")

        artesano["id"]         = id_artesano
        artesano["name"]       = name
        artesano["phone"]      = phone
        artesano["comuna"]     = comuna
        artesano["file"]       = f"{ruta_file}/{filename}"
        artesano["artesanias"] = ", ".join(artesanias)

        artesanos.append(artesano)

    return artesanos

def artesano(id_artesano):
    artesano = {}

    region, comuna, description, name, email, phone = db.get_artesano_by_id(id_artesano) 
    artesanias = db.get_artesanias_by_id_artesano(id_artesano)

    ruta_file, filename  = db.get_file_by_id_artesano(id_artesano)
    ruta_file = ruta_file.replace("static/","")

    artesano["name"]        = name
    artesano["email"]       = email
    artesano["phone"]       = phone
    artesano["region"]      = region
    artesano["comuna"]      = comuna
    artesano["description"] = description
    artesano["file"]        = f"{ruta_file}/{filename}"
    artesano["artesanias"]  = ", ".join(artesanias)

    return artesano


    
def hinchas(offset):
    hinchas  = []

    for id_hincha, name, comuna, transp, phone in db.get_hinchas(offset):

        hincha = {}
        sports = db.get_sports_by_id_hincha(id_hincha)

        hincha["id"]         = id_hincha
        hincha["name"]       = name
        hincha["phone"]      = phone
        hincha["comuna"]     = comuna
        hincha["sports"]     = ", ".join(sports)
        hincha["transporte"] = transp
        hinchas.append(hincha)

    return hinchas

def hincha(id_hincha):
    hincha = {}

    region, comuna, transp, name, email, phone, comment = db.get_hincha_by_id(id_hincha)
    sports = db.get_sports_by_id_hincha(id_hincha)

    hincha["region"]     = region
    hincha["comuna"]     = comuna
    hincha["transporte"] = transp
    hincha["name"]       = name
    hincha["email"]      = email
    hincha["phone"]      = phone
    hincha["sports"]     = ", ".join(sports)
    hincha["comment"]    = comment

    return hincha