Franco González

-Se utilizaron expresiones regulares para algunas validaciones.

-Los inputs con opciones vienen con sin valor, para que el usuario este obligado a ingresar algo.

-La expresion regular para el correo la encontre aqui:
"https://stackoverflow.com/questions/5861332/pattern-matching-email-address-using-regular-expressions".

-No estaba seguro de que formato debían seguir por lo que acepta solo números de 11 dígitos que comiencen
con 569 o números de 9 dígitos que comiencen con 9 o números de 8 dígitos cualquiera. El input númerico no
acepta espacios. El input permite "+" y "-" pero al obtener el '.value' del input no lo entrega con estos
caracteres.

-La validacion del nombre se asegura que usemos letras o _, y que no tenga espacios al inicio y al final,
 y que tampoco tenga espacio dobles entre palabras.

-Las demás validaciones en general se aseguran de que se ingrese algo.

-Para los deportes y artesanias, aquellos elementos que se seleccionene se irán guardando en una lista
visible abajo del input, si se selecciona 2 veces un mismo elemento se borra de la lista y si se
seleccionan más de 3 elementos se borrará el primer elemento en entrar a la lista.

-Al presionar el botón para registrarse, se irán validando todos los inputs en orden, si encuentra uno que
este mal entonces se alertará el error y se detendrá la validación. Se tendrá que ingresar un input correcto
y volver a presionar el botón de registro para que el input deje de mostrar error.