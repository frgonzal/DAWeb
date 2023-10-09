let selectedSports = [];


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
        validateSports(sports,selectedSports) &&
        validateRegion(region)                &&
        validateComuna(comuna)                &&
        validateTransport(transp)             &&
        validateName(name)                    &&
        validateEmail(email)                  &&
        validatePhoneNumber(phone)            &&
        validateComment(comment)
    )
        return true; 
    return false;
};
let submitBtn = document.getElementById("submitBtn");
submitBtn.addEventListener("click", validate);
//-----------------------------------------------


let addSportOption = document.getElementById("sports");
const addSport = () => {
    document.getElementById("showSelectedSports").hidden = false;
    let sportList = document.getElementById("showSelectedSportsList");
    let sportVal = addSportOption.value;
    if(sportVal.length > 0){
        if(!selectedSports.includes(sportVal))
            selectedSports.push(sportVal);
        else
            selectedSports.splice(selectedSports.indexOf(sportVal),1);
    }
    if(selectedSports.length>3)
        selectedSports.shift();
    sportList.innerHTML = "";
    for(const sport of selectedSports){
        sportList.innerHTML += "<li>"+sport+"</li>";
    }
    addSportOption.value = "";
};
addSportOption.addEventListener("input", addSport);


//opciones de input
setDeportes();
setTransp();

let regiones = document.getElementById("regiones");
regiones.value = "";
regiones.addEventListener("input", setComunas);


let btnConfirmar = document.getElementById("confirmar");
btnConfirmar.addEventListener("click", postForm);

let btnRechazar  = document.getElementById("rechazar");
btnRechazar.addEventListener("click", formRechazar);


document.getElementById("confirmacionSubmit").style.display = "none";