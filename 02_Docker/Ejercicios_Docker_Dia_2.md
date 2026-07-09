# Ejercicios Docker Día 2

## Objetivo

Pasar de `docker run` a [[Docker_Compose]] y entender redes/volúmenes.

## Compose de Qdrant

Crea `docker-compose.yml` en una carpeta de pruebas:

```yaml
services:
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

volumes:
  qdrant_data:
```

Ejecuta:

```bash
docker compose up -d
docker compose ps
docker compose logs -f
```

Comprueba en navegador: `http://localhost:6333/dashboard`

Para parar:

```bash
docker compose down
```

## Autocomprobación

- [ ] ¿Qué se pierde si hago `docker compose down -v`?
- [ ] ¿Qué puerto usa mi host?
- [ ] ¿Qué puerto usa Qdrant dentro?

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
