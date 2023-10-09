Franco González


====================
TAREA 2
====================

- Ahora para artesanias, se muestran varias opciones y se puede seleccionar más de una con ctrl+click_izq,
se guardaran todos los elementos seleccionados y se motraran todos al ver la información del artesano.

- Al agregar un artesano, se guardaran todos los archivos que se seleccionaron, pero al mostrar la información
no se mostraran todas las imagenes subidas (solo por diseño de la aplicación).


====================
TAREA 1
====================

- Se utilizaron expresiones regulares para algunas validaciones.

- Los inputs con opciones vienen sin valor, para que el usuario este obligado a ingresar algo.

- La expresion regular para el correo la encontre aqui:
"https://stackoverflow.com/questions/5861332/pattern-matching-email-address-using-regular-expressions".

- Se utilizo una expresion regular para los números de teléfono. El formato que deben tener los numeros de teléfono
es: +56 9 XXXX-XXXX. Se puede omitir el '56', el '56 9', el '+', los espacios y el guion.
"https://es.wikipedia.org/wiki/Anexo:Prefijos_telef%C3%B3nicos_de_Chile"

- La validacion del nombre se asegura que usemos letras o _, y que no tenga espacios al inicio y al final,
 y que tampoco tenga espacio dobles entre palabras.

- Las demás validaciones en general se aseguran de que se ingrese algo.

- Para los deportes, aquellos elementos que se seleccionene se irán guardando en una lista
visible abajo del input, si se selecciona 2 veces un mismo elemento se borra de la lista y si se
seleccionan más de 3 elementos se borrará el primer elemento en entrar a la lista.

- Al presionar el botón para registrarse, se irán validando todos los inputs en orden, si encuentra uno que
este mal entonces se alertará el error y se detendrá la validación. Se tendrá que ingresar un input correcto
y volver a presionar el botón de registro para que el input deje de mostrar error.
