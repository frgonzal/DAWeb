from database.conn import get_conn
from database.querys import QUERY_DICT
  


######################
######## GET #########
######################

###   HINCHAS   ###

def get_hincha_by_id(id_hincha):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_hincha_by_id"], (id_hincha,))
    hinchas = cursor.fetchone()
    conn.close()
    return hinchas   

def get_hinchas(offset):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_hinchas_offset"], (offset,))
    hinchas = cursor.fetchall()
    conn.close()
    return hinchas


###   SPORTS   ###

def get_sports():
    sports = []
    conn   = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_sports"])
    sport = cursor.fetchone()
    while(sport):
        sports.append(sport[0])
        sport = cursor.fetchone()
    conn.close()
    return sports

def get_sports_by_id_hincha(id_hincha):
    sports = []
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_sports_by_id_hincha"], (id_hincha,))
    sport = cursor.fetchone()
    while(sport):
        sports.append(sport[0])
        sport = cursor.fetchone()
    conn.close()
    return sports

def get_sport_id_by_name(sport):
    conn   = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_sport_id_by_name"], (sport,))
    id_sport = cursor.fetchone()[0]
    conn.close()
    return id_sport


#######################
####### INSERT ########
#######################

def insert_hincha(comuna, transp, name, email, phone, comment):
    conn = get_conn()
    cursor = conn.cursor()
    ## obtener comuna del hincha
    cursor.execute(QUERY_DICT["get_comuna_id_by_name"], (comuna,))
    comuna_id = cursor.fetchone()[0]
    ## insertar hincha
    cursor.execute(QUERY_DICT["insert_hincha"], (comuna_id, transp, name, email, phone, comment))
    ## devolver hincha id    
    cursor.execute(QUERY_DICT["get_last_id"],)
    hincha_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return hincha_id

def insert_hincha_deporte(artesano_id, sport):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_sport_id_by_name"], (sport,))
    sport_id = cursor.fetchone()[0]
    cursor.execute(QUERY_DICT["insert_hincha_deporte"], (artesano_id, sport_id))
    conn.commit()
    conn.close()
