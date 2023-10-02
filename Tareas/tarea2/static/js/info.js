const persona1 = () => {
    localStorage.setItem("persona", "1");
    info();
};
const persona2 = () => {
    localStorage.setItem("persona", "2");
    info();
};
const persona3 = () => {
    localStorage.setItem("persona", "3");
    info();
};
const persona4 = () => {
    localStorage.setItem("persona", "4");
    info();
};
const persona5 = () => {
    localStorage.setItem("persona", "5");
    info();
};


const verListado = () => {
    let btnPersona1 = document.getElementById("persona1");
    btnPersona1.addEventListener("click", persona1);

    let btnPersona2 = document.getElementById("persona2");
    btnPersona2.addEventListener("click", persona2);

    let btnPersona3 = document.getElementById("persona3");
    btnPersona3.addEventListener("click", persona3);

    let btnPersona4 = document.getElementById("persona4");
    btnPersona4.addEventListener("click", persona4);

    let btnPersona5 = document.getElementById("persona5");
    btnPersona5.addEventListener("click", persona5);
};

const verInfo = () => {
    for(const x of [1,2,3,4,5]){
        document.getElementById("persona"+x).style.display = "none";
    };

    let persona = localStorage.getItem("persona");
    let contenedor = document.getElementById("persona"+persona);
    contenedor.style.display = "flex";

    let imagen = document.getElementById("grande"+persona);
    const agrandarFoto = () => {
        contenedor.style.display = "none";
        imagen.style.display  = "flex"; 
    }
    const reducirFoto = () => {
        contenedor.style.display = "flex";
        imagen.style.display = "none";
    };
    document.getElementById("imagen"+persona).addEventListener("click", agrandarFoto);
    document.getElementById("grande"+persona).addEventListener("click", reducirFoto);
};

