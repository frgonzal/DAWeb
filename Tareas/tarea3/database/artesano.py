from database.conn import get_conn
from database.querys import QUERY_DICT

""" GET """
def get_artesano_by_id(id_artesano):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesano_by_id"], (id_artesano,))
    artesano = cursor.fetchone()
    conn.close()
    return artesano

def get_artesania_id_by_name(artesania):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesania_id_by_name"], (artesania,))
    id_artesania = cursor.fetchone()
    conn.close()
    return id_artesania

def get_artesanias():
    artesanias = []
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesanias"])
    artesania = cursor.fetchone()
    while(artesania):
        artesanias.append(artesania[0])
        artesania = cursor.fetchone()
    conn.close()
    return artesanias

def get_artesanos(n):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesanos_offset"], (n,))
    artesanos = cursor.fetchall()
    conn.close()
    return artesanos

def get_artesanias_by_id_artesano(id_artesano):
    artesanias = []
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesanias_by_id_artesano"], (id_artesano,))
    artesania = cursor.fetchone()
    while(artesania):
        artesanias.append(artesania[0])
        artesania = cursor.fetchone()
    conn.close()
    return artesanias

def get_file_by_id_artesano(id_artesano):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_file_by_id_artesano"], (id_artesano,))
    file = cursor.fetchone()
    conn.close()
    return file





""" INSERT """

def insert_artesano(comuna, descripcion, nombre, email, celular):
    conn = get_conn()
    cursor = conn.cursor()
    ## obtener comuna del artesano
    cursor.execute(QUERY_DICT["get_comuna_id_by_name"], (comuna,))
    comuna_id = cursor.fetchone()[0]
    ## insertar artesano
    cursor.execute(QUERY_DICT["insert_artesano"], (comuna_id, descripcion, nombre, email, celular))
    ## devolver artesano id    
    cursor.execute(QUERY_DICT["get_last_id"],)
    artesano_id = cursor.fetchone()[0]

    conn.commit()
    conn.close()
    return artesano_id

def insert_foto(ruta_archivo, nombre_archivo, artesano_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["insert_foto"], (ruta_archivo, nombre_archivo, artesano_id))
    conn.commit()
    conn.close()

def insert_artesano_tipo(artesano_id, artesania):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_artesania_id_by_name"], (artesania,))
    tipo_artesania_id = cursor.fetchone()
    cursor.execute(QUERY_DICT["insert_artesano_tipo"], (artesano_id, tipo_artesania_id))
    conn.commit()
    conn.close()