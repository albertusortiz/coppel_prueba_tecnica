# Microservicios de Marvel

## Microservicio 1

Este servicio le permite al usuario buscar un personaje o un comic mediante una palabra. En caso de no existir coincidencias, retornamos una lista ordenada de todos los personajes,

## Microservicio 2

Este servicio permite interacciones de datos con el usuario. Por ejemplo, podremos registrarnos, hacer login y consultar a todos los usuarios registrados.

# Ejecutar los servicios

Primero debemos clonar este repositiorio en nuestro equipo local, se recomienda crear una carpeta llamada **workspace** y dentro de esta carpeta ejecutar el siguiente comando:

- git clone https://github.com/albertusortiz/coppel_prueba_tecnica.git

O en su defecto, descargar el archivo ZIP dando clic en el boton verde CODE y en la ultima opción damos clic. Descomprimimos este archivo en nuestra carpeta workspace y listo.

Ahora bien, una vez tengamos este respositorio en nuestro equipo local, ya sea que lo hayamos clonado o descargado como .zip. Podemos pasar a la siguiente seccion de Docker Compose.

# Docker Compose

En esta seccion vamos a levantar/ejecutar los micro-servicios que tenemos para este proyecto ejecutando los siguientes comandos:

Abrimos la terminal y ejecutamos los siguientes comandos(asegurate de tener Docker instalado):

### Construimos los contenedores

docker-compose build

### Ejecutamos los microservicios

docker-compose up

Una vez listo, veras en tu terminal unos procesos ejecutandoce, para finalizarlos, presiona CTRL+D.

# Probar en Postman

Ahora bien, los servicios los podemos testear desde la coleccion que puedes encontrar en la carpeta postman/. Pero basicamente los endpoints que tenemos disponibles son los siguientes:

- Para el servicio de busqueda, contamos con los siguientes endpoints desde el puerto 3030:

http://localhost:3030/searchComics/<search>

http://localhost:3030/searchComics/character/<search>

http://localhost:3030/searchComics/comic/<search>

- Para el servicio de usuarios, contamos con los siguientes endpoints desde el puerto 6060:

http://localhost:6060/users

http://localhost:6060/login
