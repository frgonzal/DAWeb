let selectedCrafts = [];


const validateForm = () =>{
    let region      = document.getElementById("regiones");
    let comuna      = document.getElementById("comunas");
    let crafts      = document.getElementById("crafts");
    let description = document.getElementById("description");
    let name        = document.getElementById("name");
    let email       = document.getElementById("email");
    let phone       = document.getElementById("phone");
    
    if(
        validateRegion(region)               &&
        validateComuna(comuna)               &&
        validateCraft(crafts,selectedCrafts) &&
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

let addCraftOption = document.getElementById("crafts");
const addCraft = () => {
    document.getElementById("showSelectedCrafts").hidden = false;
    let craftList = document.getElementById("showSelectedCraftsList");
    let craftVal  = addCraftOption.value;
    if(craftVal.length > 0){
        if(Artesanias.includes(craftVal) && !selectedCrafts.includes(craftVal))
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
document.getElementById("crafts").value = "";
let regiones = document.getElementById("regiones");
regiones.value = "";
regiones.addEventListener("input", setComunas);

let btnRechazar  = document.getElementById("rechazar");
btnRechazar.addEventListener("click", formRechazar);

let btnConfirmar = document.getElementById("confirmar");
btnConfirmar.addEventListener("click", postForm);

document.getElementById("confirmacionSubmit").style.display = "none";