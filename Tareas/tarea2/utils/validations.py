import re
import filetype


def validate_artesano(form):
    region  = form.get("regiones")
    comuna  = form.get("comunas")
    artesan = form.get("crafts")
    descrip = form.get("description")
    name    = form.get("name")
    email   = form.get("email")
    phone   = form.get("phone")
    return  (
                validate_region(region)     and validate_comuna(comuna)       and
                validate_artesania(artesan) and validate_description(descrip) and
                validate_name(name)         and validate_email(email)         and
                validate_phone(phone)
             )

def validate_region(region):
    return True

def validate_comuna(comuna):
    return True

def validate_artesania(artesania):
    return True

def validate_description(description):
    return True


def validate_name(name):
    pattern = r"^[\w]+([ ]{0,1}[\w]+)*$"
    return 3<len(name)<81 and bool(re.match(pattern, name))

def validate_email(email):
    pattern = r"^(?:(?!.*?[.]{2})[a-zA-Z0-9](?:[a-zA-Z0-9.+!%-]{1,64}|)|\"[a-zA-Z0-9.+!% -]{1,64}\")@[a-zA-Z0-9][a-zA-Z0-9.-]+(.[a-z]{2,}|.[0-9]{1,})$"
    return 0<len(email)<31 and "@" in email and bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r"^(([+]{0,1}5{1}6{1}[ ]{0,1}9{1}[ ]{0,1})|(9{1}[ ]{0,1})|())[1234567890]{4}[-]{0,1}[1234567890]{4}$|^$"
    return (len(phone)==0) or (7<len(phone)<16 and bool(re.match(pattern, phone)))

def validate_files(files):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
    # check if a file was submitted
    if files is None:
        return False
    # check if the browser submitted an empty file
    if files.filename == "":
        return False
    # check file extension
    ftype_guess = filetype.guess(files)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True






    



