// se buscan los elementos necesarios
// --> PROGRAME AQUI!<---
let contador = document.getElementById("contador"); 
let button_suma = document.getElementById("btn-suma");
let button_resta = document.getElementById("btn-resta");

let n = 0; // contador

const suma = () => {
    // --> PROGRAME AQUI!<---
    n += 1;
    contador.innerHTML = n;
};

const resta = () => {
    // --> PROGRAME AQUI!<---
    n -= 1;
    contador.innerHTML = n;
};
// asignar respectivamente la funciones al evento "click"
// --> PROGRAME AQUI!<---
    button_suma.addEventListener("click",suma);
    button_resta.addEventListener("click",resta);