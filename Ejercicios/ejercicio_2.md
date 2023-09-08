# Ejercicio 2
**Nombre**: [Franco González Leiva]

---

## Observaciones
Tenga en cuenta las siguientes observaciones al realizar el ejercicio:

- El ejercicio es de carácter **personal**; la copia será penalizada con **nota mínima**.
- De ser necesario investigar, usted esta **autorizado a utilizar internet** como herramienta.
- El uso de modelos generativos de lenguaje como **ChatGPT está estrictamente prohibido** y será penalizado con **nota mínima**. 

## Pregunta 1

¿Qué es el ataque de "Cross-Site Scripting" (XSS) y cómo podría prevenirse en el desarrollo front-end? Describa un escenario en el cual este tipo de ataque podría ser especialmente peligroso.

**Respuesta**:

El ataque XSS consiste en inyectar código malisioso en una web confiable, código que puede ser ejecutado por algun usuario de la aplicación web. Para prevenir un ataque XSS se tendría que revisar los formularios que se reciben y comprobar que no contengan ningún script ejecutable, solo despues de comprobar que el no contiene scripts se acepta el formulario para ser enviado.

Un escenario especialmente peligroso sería que el atacante deje un script en la aplicación y que este, al ser ejecutado por un usuario, envie información personal y claves del usuario al atacante, lo que pondría en gran riesgo al usuario.



## Pregunta 2
Existen variadas librerías y *frameworks* de Javascript que se pueden utilizar para programar tareas más complejas en el Frontend y manipular el DOM con mayor facilidad. Investigue, nombre y describa 3 de las librerías o Frameworks de javascript más usados en el desarrollo web (por ejemplo, **JQuery**). Si tuviese que implementar su página web ¿Cuál utilizaría?   

**Respuesta**:

- React.js:

Es una biblioteca de JavaScript que se utiliza para crear interfaces de usuario. Es facil de aprender y tiene una sólida documentación. React permite trabajar con componentes reutilizables que conforman partes de la interfaz de usuario. Cuenta con un DOM virtual que permite que la renderización de las páginas sea más rápida. También es ampliamente extensible.

- AngularJS:

Framework de JavaScript de codigo abierto. Utilizado para crear y mantener aplicaciones web de una sola página. AngularJS utiliza la arquitectura Modelo-Vista-Controlador. Posee un alro rendimiento, es fácil y rápido de adoptar, permite pruebas frecuentes, etc.  

- Node.js:

Es un marco de trabajo de JavaScript del lado del servidor. Es un entorno de ejecución que ejecuta códigos JS fuera de un navegador. Esta diseñado para ayudar a desarrollar aplicaciones del lado del servidor escalables, rápidas y fiables basadas en la red.


Para implementar una página web probablemente utilizaria React.js, ya que parece ser la más simple de implementar y ofrece lo necesario para obtener un buen resultado.
