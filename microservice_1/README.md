# Microservicio para buscar un personaje o un comic.

## Construir la iamgen

docker build -t servicio_buscar .

## Ejecutar la imagen

docker run -it --publish 3030:4000 servicio_buscar

## Probar en Postman

http://localhost:3030/searchComics/<buscar_personaje_comic>
