let selectedSports = [];

const validateFormHincha = () =>{
    let sports  = document.getElementById("sports");
    let region  = document.getElementById("regiones");
    let comuna  = document.getElementById("comunas");
    let transp  = document.getElementById("transporte");
    let name    = document.getElementById("name");
    let email   = document.getElementById("email");
    let phone   = document.getElementById("numero");
    let comment = document.getElementById("comentarios");

    if(     !validateSports(sports,selectedSports));
    else if(!validateRegion(region));
    else if(!validateComuna(comuna));
    else if(!validateTransport(transp));
    else if(!validateName(name));
    else if(!validateEmail(email));
    else if(!validatePhoneNumber(phone));
    else if(!validateComment(comment));
    else { 
        document.getElementById("confirmacionSubmit").style.display = "flex";
        document.getElementById("containerForm").style.display = "none";
    }
};
let submitBtn = document.getElementById("submit");
submitBtn.addEventListener("click", validateFormHincha);
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
setRegiones();
setTransp();
let regiones = document.getElementById("regiones");
regiones.addEventListener("input", setComunas);


let btnConfirmar = document.getElementById("confirmar");
btnConfirmar.addEventListener("click", formConfirmar);

let btnRechazar  = document.getElementById("rechazar");
btnRechazar.addEventListener("click", formRechazar);


let btnPortada  = document.getElementById("btnPortada");
btnPortada.addEventListener("click", html_portada);

document.getElementById("confirmacionSubmit").style.display = "none";
document.getElementById("containerRegreso").style.display = "none";