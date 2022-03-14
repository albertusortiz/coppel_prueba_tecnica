# Microservicios de Marvel

## Microservicio 1

Este servicio le permite al usuario buscar un personaje o un comic mediante una palabra. En caso de no existir coincidencias, retornamos una lista ordenada de todos los personajes,

## Microservicio 2

Este servicio permite interacciones de datos del usuario.

# Docker Compose

Para levantar los servicios ejecutaremos los siguientes comandos:

### Construimos los contenedores

docker-compose build

### Ejecutamos los microservicios

docker-compose up

# Probar en Postman

** Los servicios los podemos testear desde la coleccion que puedes encontrar en la carpeta postman/ **

- Para el servicio de busqueda, contamos con los siguientes endpoints desde el puerto 3030:

http://localhost:3030/searchComics/<search>

http://localhost:3030/searchComics/character/<search>

http://localhost:3030/searchComics/comic/<search>

- Para el servicio de usuarios, contamos con los siguientes endpoints desde el puerto 6060:

http://localhost:6060/users

http://localhost:6060/login
