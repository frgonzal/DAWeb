QUERY_DICT = {

#########  REGIONES Y COMUNAS  #########
    "get_regiones":
        """ SELECT id, nombre
            FROM region;
        """,

    "get_comunas_by_region":
        """ SELECT nombre
            FROM comuna
            WHERE region_id = %s;
        """,

    "get_region_by_name:":
        """ SELECT id, nombre
            FROM region WHERE nombre = %s;
        """, 


    "get_comuna_id_by_name":
        """ SELECT id
            FROM comuna
            WHERE nombre=%s;
        """,

    "get_comuna_by_region_and_name":
        """ SELECT comuna.id, comuna.nombre
            FROM comuna AS comuna,
                 region AS region
            WHERE region.id=comuna.region_id
            AND   region.nombre=%s
            AND   comuna.nombre=%s;
        """,

#########  ARTESANOS  #########
    "get_artesanias":
        """ SELECT nombre
            FROM tipo_artesania;
        """,

    "get_artesania_id_by_name":
        """ SELECT id
            FROM tipo_artesania
            WHERE nombre=%s;
        """,

    "get_artesanias_by_id_artesano":
        """ SELECT nombre
            FROM artesano_tipo,
                 tipo_artesania
            WHERE artesano_id=%s
            AND   tipo_artesania_id=id;
        """,

    "get_file_by_id_artesano":
        """ SELECT ruta_archivo, nombre_archivo
            FROM foto
            WHERE artesano_id=%s;
        """,

    "get_artesanos_offset":
        """ SELECT artesano.id, artesano.nombre, artesano.celular, comuna.nombre
            FROM artesano AS artesano,
                 comuna   AS comuna
            WHERE artesano.comuna_id=comuna.id
            ORDER BY artesano.id DESC
            LIMIT 5
            OFFSET %s;
        """,

    "get_artesano_by_id":
        """ SELECT reg.nombre, com.nombre, art.descripcion_artesania, art.nombre, art.email, art.celular
            FROM artesano AS art,
                 comuna   AS com,
                 region   AS reg
            WHERE art.id=%s
            AND art.comuna_id=com.id
            AND com.region_id=reg.id;
        """,

    "get_artesanos_total":
        "SELECT COUNT(*) FROM artesano;",

    "insert_artesano":
        """ INSERT INTO artesano
            (comuna_id, descripcion_artesania, nombre, email, celular)
            VALUES (%s, %s, %s, %s, %s);
        """,

    "insert_artesano_tipo":
        """ INSERT INTO artesano_tipo
            (artesano_id, tipo_artesania_id)
            VALUES (%s, %s);""",

    "insert_foto":
        """ INSERT INTO foto
            (ruta_archivo, nombre_archivo, artesano_id)
            VALUES (%s, %s, %s);
        """,

    
#########  HINCHAS  #########

### DEPORTES
    "get_sports":
        """ SELECT nombre
            FROM deporte;
        """,

    "get_sport_id_by_name":
        """ SELECT id
            FROM deporte
            WHERE nombre=%s;
        """,
    
    "get_sports_by_id_hincha":
        """ SELECT nombre
            FROM deporte,
                 hincha_deporte
            WHERE hincha_id=%s
            AND   deporte_id=id;
        """,

### HINCHAS SELECT 
    "get_hinchas_offset":
        """ SELECT hincha.id, hincha.nombre, comuna.nombre, hincha.modo_transporte, hincha.celular
            FROM hincha AS hincha,
                 comuna AS comuna
            WHERE hincha.comuna_id=comuna.id
            ORDER BY hincha.id DESC
            LIMIT 5
            OFFSET %s;
        """,

    "get_hincha_by_id":
        """ SELECT region.nombre, comuna.nombre, hincha.modo_transporte, hincha.nombre,
                   hincha.email, hincha.celular, hincha.comentarios
            FROM hincha AS hincha,
                 comuna AS comuna,
                 region AS region
            WHERE hincha.id=%s
            AND   hincha.comuna_id=comuna.id
            AND   comuna.region_id=region.id;
        """,

### HINCHAS INSERT 
    "insert_hincha":
        """ insert into hincha
            (comuna_id, modo_transporte, nombre, email, celular, comentarios)
            values (%s, %s, %s, %s, %s, %s);
        """,

    "insert_hincha_deporte":
        """ insert into hincha_deporte
            (hincha_id, deporte_id)
            values (%s, %s);
        """,


#########  EXTRA  #########
    "get_total_tabla":
        "select count(*) from ",

    "get_last_id":
        "SELECT LAST_INSERT_ID();"
}