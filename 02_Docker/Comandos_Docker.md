# Comandos Docker

## Diagnóstico

```bash
docker version
docker info
docker ps
docker ps -a
docker images
docker volume ls
docker network ls
```

## Contenedores

```bash
docker run hello-world
docker run --name demo -p 8080:80 -d nginx:alpine
docker logs demo
docker logs -f demo
docker exec -it demo sh
docker stop demo
docker rm demo
```

## Compose

```bash
docker compose up -d
docker compose down
docker compose logs -f
docker compose ps
docker compose exec <service> sh
```

## Lectura rápida

- `ps`: qué está vivo.
- `ps -a`: también lo muerto.
- `logs`: por qué falló.
- `exec`: qué hay dentro.
- `inspect`: verdad completa, aunque verbosa.

## Lección guiada

En Docker, cada concepto debe aterrizar en un comando observable. No basta con decir "contenedor": debes saber verlo, pararlo, inspeccionarlo y leer sus logs.

### Preguntas

- ¿Qué vive en la imagen y qué vive en el contenedor?
- ¿Qué parte se pierde al borrar el contenedor?
- ¿Qué URL usa mi host y qué URL usa otro contenedor?
- ¿Qué log confirma que el servicio arrancó?

### Práctica

```bash
docker ps
docker ps -a
docker logs <container>
docker exec -it <container> sh
docker compose ps
docker compose logs -f
```

### Evidencia

- [ ] He ejecutado al menos un comando relacionado con esta nota.
- [ ] Puedo explicar un fallo típico.
- [ ] Sé cómo conectarlo con [[Docker_para_OpenWebUI_Qdrant_LiteLLM]].
