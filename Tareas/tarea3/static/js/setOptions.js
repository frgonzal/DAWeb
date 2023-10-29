const setComunas = () => {
    let regiones = document.getElementById("regiones");
    let comunas  = document.getElementById("comunas");
    comunas.innerHTML = "";

    for(let comuna of Comunas[regiones.value]){
        comunas.innerHTML += "<option>"+comuna+"</option>";
    }
    comunas.value = "";
};