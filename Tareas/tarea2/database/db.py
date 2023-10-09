import pymysql
import json


DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('database/querys.json', 'r') as querys:
    QUERY_DICT = json.load(querys)

def get_conn():
    conn = pymysql.connect(
        db=DB_NAME,
        user=DB_USERNAME,
        passwd=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        charset=DB_CHARSET
    )
    return conn



""" SELECT """

def get_artesano_by_id(id_artesano):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesano_by_id"], (id_artesano, ))
    artesano = cursor.fetchone()
    return artesano

def get_regiones():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_regiones"])
    regiones = cursor.fetchall()
    return regiones

def get_comunas_by_region(id_region):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_comunas_by_region"], (id_region,))
    comunas = cursor.fetchall()
    return comunas

def get_comuna_by_region_and_name(region, comuna):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_comuna_by_region_and_name"], (region, comuna))
    comuna = cursor.fetchone()
    return comuna

def get_artesania_id_by_name(artesania):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesania_id_by_name"], (artesania))
    id_artesania = cursor.fetchone()
    return id_artesania

def get_artesanias():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesanias"])
    artesanias = cursor.fetchall()
    return artesanias

def get_artesanos(n):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesanos_offset"], (n,))
    artesanos = cursor.fetchall()
    return artesanos

def get_artesanias_by_id_artesano(id_artesano):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesanias_by_id_artesano"], (id_artesano,))
    artesanias = cursor.fetchall()
    return artesanias

def get_file_by_id_artesano(id_artesano):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_file_by_id_artesano"], (id_artesano,))
    file = cursor.fetchone()
    return file

def get_artesanos_total():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesanos_total"], )
    total = cursor.fetchone()
    return total



""" INSERT """

def insert_artesano(comuna, descripcion, nombre, email, celular):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_comuna_id_by_name"], (comuna))
    comuna_id = cursor.fetchone()
    cursor.execute(QUERY_DICT["insert_artesano"], (comuna_id, descripcion, nombre, email, celular))
    cursor.execute(QUERY_DICT["get_last_id"],)
    artesano_id = cursor.fetchone()
    conn.commit()
    return artesano_id

def insert_foto(ruta_archivo, nombre_archivo, artesano_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["insert_foto"], (ruta_archivo, nombre_archivo, artesano_id))
    conn.commit()

def insert_artesano_tipo(artesano_id, artesania):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesania_id_by_name"], (artesania,))
    tipo_artesania_id = cursor.fetchone()
    cursor.execute(QUERY_DICT["insert_artesano_tipo"], (artesano_id, tipo_artesania_id))
    conn.commit()




