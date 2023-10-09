from database import db
import re
import filetype


def validate_artesano(
        region,
        comuna,
        artesanias,
        description,
        name,
        email,
        phone,
        files
    ):
    error = []
    if not validate_reg_com(region, comuna):  error.append("Region y Comuna") 
    if not validate_artesania(artesanias):    error.append("Tipo artesanía ")
    if not validate_description(description): error.append("Descripción artesanías")
    if not validate_files(files):             error.append("Fotos artesanías")
    if not validate_name(name):               error.append("Nombre artesano(a)")
    if not validate_email(email):             error.append("Email contacto artesano(a) ")
    if not validate_phone(phone):             error.append("Número celular contacto")
    return error


def validate_reg_com(region, comuna):
    return True if db.get_comuna_by_region_and_name(region, comuna) else False

def validate_artesania(artesanias):
    for artesania in artesanias:
        if not db.get_artesania_id_by_name(artesania):
            return False
    return True

def validate_description(description):
    return 0 <= len(description) <= 300

def validate_name(name):
    pattern = r"^[\w]+([ ]{0,1}[\w]+)*$"
    return 3 <= len(name) <= 80 and bool(re.match(pattern, name))

def validate_email(email):
    pattern = r"^(?:(?!.*?[.]{2})[a-zA-Z0-9](?:[a-zA-Z0-9.+!%-]{1,64}|)|\"[a-zA-Z0-9.+!% -]{1,64}\")@[a-zA-Z0-9][a-zA-Z0-9.-]+(.[a-z]{2,}|.[0-9]{1,})$"
    return 1 <= len(email) <= 30 and ("@" in email) and bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r"^(([+]{0,1}5{1}6{1}[ ]{0,1}9{1}[ ]{0,1})|(9{1}[ ]{0,1})|())[1234567890]{4}[-]{0,1}[1234567890]{4}$|^$"
    return (len(phone)==0) or (7<len(phone)<16 and bool(re.match(pattern, phone)))

def validate_files(files):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif", "image/pdf"}

    if not files:
        return False

    for file in files:
        if file.filename == "":
            return False
        ftype_guess = filetype.guess(file)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False
    return True






    



