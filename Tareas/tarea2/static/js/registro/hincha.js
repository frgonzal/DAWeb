const validateForm = () =>{
    let sports  = document.getElementById("sports");
    let region  = document.getElementById("regiones");
    let comuna  = document.getElementById("comunas");
    let transp  = document.getElementById("transporte");
    let name    = document.getElementById("name");
    let email   = document.getElementById("email");
    let phone   = document.getElementById("phone");
    let comment = document.getElementById("comentarios");

    if(
        validateSports(sports)     &&
        validateRegion(region)     &&
        validateComuna(comuna)     &&
        validateTransport(transp)  &&
        validateName(name)         &&
        validateEmail(email)       &&
        validatePhoneNumber(phone) &&
        validateComment(comment)
    )
        return true; 
    return false;
};
let submitBtn = document.getElementById("submitBtn");
submitBtn.addEventListener("click", validate);
//-----------------------------------------------

setDeportes();
setTransp();

let sports = document.getElementById("sports");
sports.value = "";

let regiones = document.getElementById("regiones");
regiones.value = "";
regiones.addEventListener("input", setComunas);

let btnConfirmar = document.getElementById("confirmar");
btnConfirmar.addEventListener("click", postForm);

let btnRechazar  = document.getElementById("rechazar");
btnRechazar.addEventListener("click", formRechazar);

document.getElementById("confirmacionSubmit").style.display = "none";