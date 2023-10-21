const validateForm = () =>{
    let region      = document.getElementById("regiones");
    let comuna      = document.getElementById("comunas");
    let crafts      = document.getElementById("crafts");
    let description = document.getElementById("description");
    let name        = document.getElementById("name");
    let email       = document.getElementById("email");
    let phone       = document.getElementById("phone");    
    let files       = document.getElementById("files");

    if(
        validateRegion(region)               &&
        validateComuna(comuna)               &&
        validateCraft(crafts)                &&
        validateDescription(description)     &&
        validateFiles(files)                 &&
        validateName(name)                   &&
        validateEmail(email)                 &&
        validatePhoneNumber(phone)
    )
        return true;
    return false;
};

let submitBtn = document.getElementById("submitBtn");
submitBtn.addEventListener("click", validate);
//-----------------------------------------------

let artesanias = document.getElementById("crafts")
artesanias.value = "";

let regiones = document.getElementById("regiones");
regiones.value = "";
regiones.addEventListener("input", setComunas);

let btnRechazar  = document.getElementById("rechazar");
btnRechazar.addEventListener("click", formRechazar);

let btnConfirmar = document.getElementById("confirmar");
btnConfirmar.addEventListener("click", postForm);

document.getElementById("confirmacionSubmit").style.display = "none";