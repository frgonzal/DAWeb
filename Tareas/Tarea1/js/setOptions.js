const Sports = [
    "Clavados", "Natación", "Natación artística", "Polo acuático", "Natación en Aguas abiertas", "Maratón", "Marcha", "Atletismo", "Bádminton", "Balonmano", "Básquetbol", "Básquetbol 3x3",
    "Béisbol", "Boxeo", "Bowling", "Breaking", "Canotaje Slalom", "Canotaje de velocidad", "BMX Freestyle", "BMX Racing", "Mountain Bike", "Ciclismo pista", "Ciclismo ruta",
    "Adiestramiento ecuestre", "Evento completo ecuestre", "Salto ecuestre", "Escalada deportiva", "Esgrima", "Esquí acuático y Wakeboard", "Fútbol", "Gimnasia artística Masculina", "Gimnasia artística Femenina",
    "Gimnasia rítmica", "Gimnasia trampolín", "Golf", "Hockey césped", "Judo", "Karate", "Levantamiento de pesas", "Lucha", "Patinaje artístico", "Skateboarding", "Patinaje velocidad", "Pelota vasca", "Pentatlón moderno",
    "Racquetball", "Remo", "Rugby 7", "Sóftbol", "Squash", "Surf", "Taekwondo", "Tenis", "Tenis de mesa", "Tiro", "Tiro con arco", "Triatlón", "Vela", "Vóleibol", "Vóleibol playa"
];
const Regiones = [
    "Aisén del G. Carlos Ibáñez del Campo", "Antofagasta", "Arica y Parinacota", "Atacama", "Biobío", "Coquimbo", "La Araucanía", "Libertador General Bernardo O'Higgins",
    "Los Lagos", "Los Ríos", "Magallanes y de la Antártica Chilena", "Maule", "Metropolitana de Santiago", "Ñuble", "Tarapacá", "Valparaíso"
];
const Comunas = {
    "":"",
    "Aisén del G. Carlos Ibáñez del Campo":["Guaitecas","Cisnes","Lago Verde","Coyhaique","Aysén","Río Ibáñez","Chile Chico","Cochrane","O'Higgins", "Tortel"],
    "Antofagasta":["Antofagasta","Mejillones","Sierra Gorda","Taltal","Calama","Ollagüe","San Pedro de Atacama","María Elena","Tocopilla"],
    "Arica y Parinacota":["Arica","Putre","General Lagos","Camarones"],
    "Atacama":["Chañaral","Diego de Almagro","Caldera","Copiapó","Tierra Amarilla","Alto del Carmen","Freirina","Huasco","Vallenar"],
    "Biobío":["Arauco","Cañete","Contulmo","Curanilahue","Lebu","Los Álamos","Tirúa","Alto Biobío","Antuco","Cabrero","Laja","Los Ángeles","Mulchén","Nacimiento","Negrete","Quilaco","Quilleco","San Rosendo","Santa Bárbara",
                "Tucapel","Yumbel","Chiguayante","Concepción","Coronel","Florida","Hualpén","Hualqui","Lota","Penco","San Pedro de la Paz","Santa Juana","Talcahuano","Tomé"],
    "Coquimbo":["Canela","Illapel","Los Vilos","Salamanca","Andacollo","Coquimbo","La Higuera","La Serena","Paihuano","Vicuña","Combarbalá","Monte Patria","Ovalle","Punitaqui","Río Hurtado"],
    "La Araucanía":["Carahue","Cholchol","Cunco","Curarrehue","Freire","Galvarino","Gorbea","Lautaro","Loncoche","Melipeuco","Nueva Imperial","Padre Las Casas","Perquenco","Pitrufquén","Pucón","Saavedra","Temuco",
                    "Teodoro Schmidt","Toltén","Vilcún","Villarrica","Angol","Collipulli","Curacautín","Ercilla","Lonquimay","Los Sauces","Lumaco","Purén","Renaico","Traiguén","Victoria"],
    "Libertador General Bernardo O'Higgins":["Codegua","Coinco","Coltauco","Doñihue","Graneros","Las Cabras","Machalí","Malloa","Mostazal","Olivar","Peumo","Pichidegua","Quinta de Tilcoco","Rancagua","Rengo","Requínoa",
                                            "San Vicente de Tagua Tagua","La Estrella","Litueche","Marchigüe","Navidad","Paredones","Pichilemu","Chépica","Chimbarongo","Lolol","Nancagua","Palmilla","Peralillo","Placilla",
                                            "Pumanque","San Fernando","Santa Cruz"],
    "Los Lagos":["Ancud","Castro","Chonchi","Curaco de Vélez","Dalcahue","Puqueldón","Queilén","Quemchi","Quellón","Quinchao","Calbuco","Cochamó","Fresia","Frutillar","Llanquihue","Los Muermos","Maullín","Puerto Montt",
                "Puerto Varas","Osorno","Puerto Octay","Purranque","Puyehue","Río Negro","San Juan de la Costa","San Pablo","Chaitén","Futaleufú","Hualaihué","Palena"],
    "Los Ríos":["Panguipulli","Futrono","Río Bueno","Lago Ranco","La Unión","Corral","Paillaco","Valdivia","Máfil","Lanco","Mariquina","Los Lagos"],
    "Magallanes y de la Antártica Chilena":["Antártica","Cabo de Hornos","Laguna Blanca","Punta Arenas","Río Verde","San Gregorio","Porvenir","Primavera","Timaukel","Natales","Torres del Paine"],
    "Maule":["Cauquenes","Chanco","Pelluhue","Curicó","Hualañé","Licantén","Molina","Rauco","Romeral","Sagrada Familia","Teno","Vichuquén","Colbún","Linares","Longaví","Parral","Retiro","San Javier de Loncomilla",
            "Villa Alegre","Yerbas Buenas","Constitución","Curepto","Empedrado","Maule","Pelarco","Pencahue","Río Claro","San Clemente","San Rafael","Talca"],
    "Metropolitana de Santiago":["Colina","Lampa","Til Til","Pirque","Puente Alto","San José de Maipo","Buin","Calera de Tango","Paine","San Bernardo","Alhué","Curacaví","María Pinto","Melipilla","San Pedro","Cerrillos",
                                "Cerro Navia","Conchalí","El Bosque","Estación Central","Huechuraba","Independencia","La Cisterna","La Granja","La Florida","La Pintana","La Reina","Las Condes","Lo Barnechea","Lo Espejo",
                                "Lo Prado","Macul","Maipú","Ñuñoa","Pedro Aguirre Cerda","Peñalolén","Providencia","Pudahuel","Quilicura","Quinta Normal","Recoleta","Renca","San Miguel","San Joaquín","San Ramón","Santiago",
                                "Vitacura","El Monte","Isla de Maipo","Padre Hurtado","Peñaflor","Talagante"],
    "Ñuble":["Cobquecura","Coelemu","Ninhue","Portezuelo","Quirihue","Ránquil","Trehuaco","Bulnes","Chillán Viejo","Chillán","El Carmen","Pemuco","Pinto","Quillón","San Ignacio","Yungay","Coihueco","Ñiquén",
            "San Carlos","San Fabián","San Nicolás"],
    "Tarapacá":["Huara","Camiña","Colchane","Pica","Pozo Almonte","Alto Hospicio","Iquique"],
    "Valparaíso":["Hanga Roa","Calle Larga","Los Andes","Rinconada","San Esteban","Cabildo","La Ligua","Papudo","Petorca","Zapallar","Hijuelas","La Calera","La Cruz","Nogales","Quillota","Algarrobo","Cartagena",
                "El Quisco","El Tabo","San Antonio","Santo Domingo","Catemu","Llay-Llay","Panquehue","Putaendo","San Felipe","Santa María","Casablanca","Concón","Juan Fernández","Puchuncaví","Quintero","Valparaíso",
                "Viña del Mar","Limache","Olmué","Quilpué","Villa Alemana"]
};

const Crafts = [ "mármol", "madera", "cerámica", "mimbre", "metal", "cuero", "telas", "joyas", "otro tipo" ]

const Transports = ["Particular","Locomoción pública"];

const setDeportes = () => {
    let deportesSelect = document.getElementById("sports");
    for(let deporte of Sports){
        deportesSelect.innerHTML += "<option>"+deporte+"</option>";
    }
    deportesSelect.value = "";
};

const setRegiones = () =>{
    let regionesSelect = document.getElementById("regiones");
    for(let region of Regiones){
        regionesSelect.innerHTML += "<option>"+region+"</option>";
    }
    regionesSelect.value = "";
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
