from database import db
from flask import url_for

def regiones_comunas():
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
    return regiones, comunas


def artesanias():
    artesanias = []
    for art in db.get_artesanias():
        _, artesania = art
        artesanias.append(artesania)
    return artesanias

def artesanos(offset):
    artesanos = []
    artesanos_ = db.get_artesanos(offset)

    for artesano_ in artesanos_:
        artesano = {}

        id_artesano, name, phone, comuna = artesano_

        artesanias = db.get_artesanias_by_id_artesano(id_artesano)
        _, filename  = db.get_file_by_id_artesano(id_artesano)

        artesano["id"]         = id_artesano
        artesano["name"]       = name
        artesano["phone"]      = phone
        artesano["comuna"]     = comuna
        artesano["file"]       = f"uploads/{filename}"
        artesano["artesanias"] = ", ".join([artes_[0] for artes_ in artesanias])

        artesanos.append(artesano)

    return artesanos

def artesano(id_artesano):
    artesano = {}

    region, comuna, description, name, email, phone = db.get_artesano_by_id(id_artesano) 
    artesanias = db.get_artesanias_by_id_artesano(id_artesano)
    _, filename  = db.get_file_by_id_artesano(id_artesano)

    artesano["name"]        = name
    artesano["email"]       = email
    artesano["phone"]       = phone
    artesano["region"]      = region
    artesano["comuna"]      = comuna
    artesano["description"] = description
    artesano["file"]        = f"uploads/{filename}"
    artesano["artesanias"]  = ", ".join([artes_[0] for artes_ in artesanias])

    return artesano


    