const Sports = [
    "Clavados", "Natación", "Natación artística", "Polo acuático", "Natación en Aguas abiertas", "Maratón", "Marcha", "Atletismo", "Bádminton", "Balonmano", "Básquetbol", "Básquetbol 3x3",
    "Béisbol", "Boxeo", "Bowling", "Breaking", "Canotaje Slalom", "Canotaje de velocidad", "BMX Freestyle", "BMX Racing", "Mountain Bike", "Ciclismo pista", "Ciclismo ruta",
    "Adiestramiento ecuestre", "Evento completo ecuestre", "Salto ecuestre", "Escalada deportiva", "Esgrima", "Esquí acuático y Wakeboard", "Fútbol", "Gimnasia artística Masculina", "Gimnasia artística Femenina",
    "Gimnasia rítmica", "Gimnasia trampolín", "Golf", "Hockey césped", "Judo", "Karate", "Levantamiento de pesas", "Lucha", "Patinaje artístico", "Skateboarding", "Patinaje velocidad", "Pelota vasca", "Pentatlón moderno",
    "Racquetball", "Remo", "Rugby 7", "Sóftbol", "Squash", "Surf", "Taekwondo", "Tenis", "Tenis de mesa", "Tiro", "Tiro con arco", "Triatlón", "Vela", "Vóleibol", "Vóleibol playa"
];

const Crafts = [ "mármol", "madera", "cerámica", "mimbre", "metal", "cuero", "telas", "joyas", "otro tipo" ]

const Transports = ["Particular","Locomoción pública"];

const setDeportes = () => {
    let deportesSelect = document.getElementById("sports");
    for(let deporte of Sports){
        deportesSelect.innerHTML += "<option>"+deporte+"</option>";
    }
    deportesSelect.value = "";
};

const setComunas = () => {
    let regionesSelect = document.getElementById("regiones");
    let comunasSelect = document.getElementById("comunas");
    comunasSelect.innerHTML = "";

    for(let comuna of Comunas[regionesSelect.value]){
        comunasSelect.innerHTML += "<option>"+comuna+"</option>";
    }
    comunasSelect.value = "";
};

const setTransp = () => {
    let transportSelect = document.getElementById("transporte");
    for(let transporte of Transports){
        transportSelect.innerHTML += "<option>"+transporte+"</option>";
    }
    transportSelect.value = "";
};

const setCrafts = () => {
    let craftsSelect = document.getElementById("crafts");
    for(const craft of Crafts){
        craftsSelect.innerHTML += "<option>"+craft+"</option>";
    }
    craftsSelect.value = "";
};
