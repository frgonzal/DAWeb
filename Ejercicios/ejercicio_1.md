# Ejercicio 1

**Nombre**: [Franco González Leiva]

---

## Pregunta 1
Explique por que el realizar validaciones del input del usuario en el front-end es una facilidad pero no una medida de seguridad. 

**Respuesta**: 
La validación en el front-end permite que el usuario tenga una mejor experiencia al utilizar la aplicación web, pero no es una medida de seguridad debido a que un usuario podría evadir la validación del front-end o enviar un input con código que se ejecutaría en el servidor, lo que pondría en riesgo la aplicación web y la base de datos.


## Pregunta 2
Usted cuenta con el siguiente codigo HTML:
```html
<div>
    <p>Contador: <span id="contador">0</span></p>
    <button type="button" id="btn-resta">-1</button>
    <button type="button" id="btn-suma">+1</button>
</div>
```
Implemente un contador bidireccional utilizando la plantilla disponible mas abajo, solo programe donde se le indica. Se espera que tras apretar un boton, el contador se actualice sin la necesidad de recargar la pagina. **No esta permitido modificar el HTML**.

**Respuesta**:
```js
// se buscan los elementos necesarios
// --> PROGRAME AQUI!<---
let contador     = document.getElementById("contador"); 
let button_suma  = document.getElementById("btn-suma");
let button_resta = document.getElementById("btn-resta");

let n = 0; // contador

const suma = () => {
    // --> PROGRAME AQUI!<---
    n += 1;
    contador.innerText = n;
};

const resta = () => {
    // --> PROGRAME AQUI!<---
    n -= 1;
    contador.innerText = n;
};
// asignar respectivamente la funciones al evento "click"
// --> PROGRAME AQUI!<---
button_suma.addEventListener("click",suma);
button_resta.addEventListener("click",resta);
```
