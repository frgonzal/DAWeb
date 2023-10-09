from database import db

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