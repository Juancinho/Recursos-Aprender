# Ejercicios Docker Día 1

## Objetivo

Entender imagen, contenedor, puerto, logs y shell dentro del contenedor.

## Pasos

```bash
docker version
docker run hello-world
docker run --name technica-nginx -p 8080:80 -d nginx:alpine
docker ps
docker logs technica-nginx
docker exec -it technica-nginx sh
```

Dentro del contenedor:

```sh
ls
cat /etc/os-release
exit
```

Después:

```bash
docker stop technica-nginx
docker rm technica-nginx
```

## Qué estás haciendo

- `docker run` crea y arranca un contenedor.
- `-d` lo deja en segundo plano.
- `-p 8080:80` publica nginx en tu host.
- `docker logs` enseña stdout/stderr del proceso.
- `docker exec` abre otro proceso dentro del contenedor.

## Entregable

- [ ] Captura o texto con `docker ps`.
- [ ] Explicación de `8080:80`.
- [ ] Una duda concreta escrita en el diario.

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
