let selectedCrafts = [];

const validateForm = () =>{
    let region      = document.getElementById("regiones");
    let comuna      = document.getElementById("comunas");
    let crafts      = document.getElementById("crafts");
    let description = document.getElementById("description");
    let name        = document.getElementById("name");
    let email       = document.getElementById("email");
    let phone       = document.getElementById("numero");
    
    if     (!validateRegion(region));
    else if(!validateComuna(comuna));
    else if(!validateCraft(crafts,selectedCrafts));
    else if(!validateDescription(description));
    else if(!validateFiles(files));
    else if(!validateName(name));
    else if(!validateEmail(email));
    else if(!validatePhoneNumber(phone));
    else{
        document.getElementById("confirmacionSubmit").style.display = "flex";
        document.getElementById("containerForm").style.display = "none";
    }
};
let submitBtn = document.getElementById("submit");
submitBtn.addEventListener("click", validateForm);
//-----------------------------------------------

let addCraftOption = document.getElementById("crafts");
const addCraft = () => {
    document.getElementById("showSelectedCrafts").hidden = false;
    let craftList = document.getElementById("showSelectedCraftsList");
    let craftVal = addCraftOption.value;
    if(craftVal.length > 0){
        if(Crafts.includes(craftVal) && !selectedCrafts.includes(craftVal))
            selectedCrafts.push(craftVal);
        else
            selectedCrafts.splice(selectedCrafts.indexOf(craftVal),1);
    }
    if(selectedCrafts.length>3)
        selectedCrafts.shift();
    craftList.innerHTML = "";
    for(const craft of selectedCrafts){
        craftList.innerHTML += "<li>"+craft+"</li>";
    }
    addCraftOption.value = "";
};
addCraftOption.addEventListener("input", addCraft);


//opciones de input
setCrafts();

let regiones = document.getElementById("regiones");
regiones.value = "";
regiones.addEventListener("input", setComunas);
console.log(Comunas);


let btnConfirmar = document.getElementById("confirmar");
btnConfirmar.addEventListener("click", formConfirmar);

let btnRechazar  = document.getElementById("rechazar");
btnRechazar.addEventListener("click", formRechazar);


let btnPortada  = document.getElementById("btnPortada");
btnPortada.addEventListener("click", html_portada);

document.getElementById("confirmacionSubmit").style.display = "none";
document.getElementById("containerRegreso").style.display = "none";