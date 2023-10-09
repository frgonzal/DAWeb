import re
import filetype


def validate_artesano(request):
    error = []
    region  = request.form.get("regiones")
    comuna  = request.form.get("comunas")
    artesan = request.form.get("crafts")
    descrip = request.form.get("description")
    name    = request.form.get("name")
    email   = request.form.get("email")
    phone   = request.form.get("phone")
    files   = request.files.get("files")


    if not validate_region(region):
        error.append("Region") 
    if not validate_comuna(comuna):
        error.append("Comuna")
    if not validate_artesania(artesan):
        error.append("Tipo artesanía ")
    if not validate_description(descrip):
        error.append("Descripción artesanías")
    if not validate_files(files):
        error.append("Fotos artesanías")
    if not validate_name(name):
        error.append("Nombre artesano(a)")
    if not validate_email(email):
        error.append("Email contacto artesano(a) ")
    if not validate_phone(phone):
        error.append("Número celular contacto")

    return error

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






    



