from database.conn import get_conn
from database.querys import QUERY_DICT

from database.artesano import *
from database.hincha   import *



""" REGIONES Y COMUNAS """

## Retorna el nombre de todas las regiones.
def get_regiones():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_regiones"])
    regiones = cursor.fetchall()
    conn.close()
    return regiones

## Retorna el nombre de todas las comunas de una región.
def get_comunas_by_region(id_region):
    comunas = []
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_comunas_by_region"], (id_region,))
    comuna = cursor.fetchone()
    while(comuna):
        comunas.append(comuna[0])
        comuna = cursor.fetchone()
    conn.close()
    return comunas

## Retorna id de una comuna con el nombre de la comuna y el nombre de la región.
## Útil para la validación.
def get_comuna_by_region_and_name(region, comuna):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_comuna_by_region_and_name"], (region, comuna))
    comuna = cursor.fetchone()
    conn.close()
    return comuna


""" OTROS """
# Retorna la cantidad de tuplas de una tabla
def get_total_tabla(tabla):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_total_tabla"]+tabla)
    total = cursor.fetchone()[0]
    conn.close()
    return total


""" GRAFICOS """
def count_hinchas_by_sport():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["count_hinchas_by_sport"])
    result = cursor.fetchall()
    conn.close()
    return result

def count_artesanos_by_artesania():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["count_artesanos_by_artesania"])
    result = cursor.fetchall()
    conn.close()
    return result