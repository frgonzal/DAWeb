# Ejercicio 4: "*Unrestricted File Upload*"

**Nombre**: Franco González Leiva

--- 
## Introduccion
Hemos enfatizado la importancia de ser extremadamente cautelosos en el manejo de la entrada de los usuarios, incluyendo los archivos. De hecho, la vulnerabilidad [*Unrestricted File Upload*](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload), la cual corresponde a confiar plenamente en los archivos subidos por el usuario, puede tener consecuencias catastróficas.

El objetivo de este ejercicio es comprender bien las posibles **consecuencias** de un manejo de archivos "mediocre" y las formas de **prevenirlas**.

## Pregunta 1
Investigue y explique **con sus propias palabras** 3 posibles ataques que un usuario malicioso podria realizar a una aplicacion web con la vulnerabilidad *Unrestricted File Upload*". Se espera que para cada ataque se mencionen las **consecuencias** del mismo.

**Respuesta:** 

- Descargar ejecutables peligrosos:  
El usuario podría enviar un archivo ejecutable que tome control del servidor. Para esto, el usuario malicioso tiene que encontrar la forma de ejecutar el archivo que envio, pero tener el archivo ejecutable en los archivos locales del servidor ya deja expuesto el servidor.

- Sobreescribir archivos locales:  
Podrían sobreescribirse archivos locales importantes o archivos que se ejecuten para que el servidor funcione, lo que le puede dar control del servidor al usuario malicioso. También pueden intentar sobreescribir archivos de otros usuarios en la aplicación, lo que puede poner en riesgo la información del usuario atacado.

- Guardar archivo en alguna ubicacion especial:  
El archivo podría terminar en otra ubicación distinta a la designada para almacenar los archivos de los usuarios, y en esa otra carpeta podría haber información que pondría en riesgo el servidor, o también podrían tomar control de la máquina en la que esta corriendo el servidor.

## Pregunta 2
Ahora que ya tenemos claro que descuidar el manejo de archivos es peligroso, les pedimos listar 5 metodos preventivos para esta vulnerabilidad.

**Respuesta:**

- Restringir los tipos de archivos que se pueden subir. Solo aceptar tipos de archivos que sean necesarios para que funcione la aplicación web. No aceptar ejecutables si nuestra aplicación no los necesita.

- Comprobar que la extension del archivo este permitida. No solo leer la extensión del archivo, también intentar adivinar la extensión con alguna función especial, ya que el archivo puede venir con una extensión permitida y ser un ejecutable.

- Comprobar que el nombre del archivo no contenga instrucciones ejecutables en el servidor, utilizando alguna función que compruebe si el nomber contiene algunos caracteres especiales que se utilicen para escribir instrucciones en alguna terminal.

- Cambiar nombre del archivo utilizando una funcion hash que reciba varios parametros del usuario, evitando así que el nombre final del archivo no sobreescriba archivos locales o que el nombre contenga instrucciones ejecutables.

- Concatenar al nombre del archivo, ya modificado por la funcion hash, un identificador único para evitar que un usuario pueda sobreescribir archivos de otros usuarios. 


