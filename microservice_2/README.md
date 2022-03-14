# Microservicio para administrar a los usuarios.

## Construir la iamgen

docker build -t servicio_usuarios .

## Ejecutar la imagen

docker run -it --publish 6060:2000 servicio_usuarios
