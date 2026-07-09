# Docker Compose

Compose define varios servicios en un YAML: OpenWebUI, Qdrant, LiteLLM, vLLM. Te evita lanzar comandos `docker run` largos y frágiles.

## Conecta con
- [[Docker]]
- [[Docker_para_OpenWebUI_Qdrant_LiteLLM]]

## Estructura mínima
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

## Comandos
```bash
docker compose up -d
docker compose ps
docker compose logs -f
docker compose down
```

## Qué mirar
Imágenes, variables de entorno, puertos, volúmenes, redes, healthchecks y command/entrypoint.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Ampliación curso: Compose como contrato de arquitectura local

Un `docker-compose.yml` no es solo un lanzador. Es una descripción de arquitectura ejecutable: qué servicios existen, cómo se llaman, qué puertos publican, qué datos persisten y qué variables los conectan.

### Ejemplo comentado

```yaml
services:
  qdrant:
    image: qdrant/qdrant:latest   # software que se ejecuta
    ports:
      - "6333:6333"               # host:contenedor
    volumes:
      - qdrant_data:/qdrant/storage

  openwebui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    environment:
      QDRANT_URI: http://qdrant:6333
      OPENAI_API_BASE_URL: http://litellm:4000/v1
    depends_on:
      - qdrant
      - litellm

volumes:
  qdrant_data:
```

### `depends_on` no significa "está listo"

`depends_on` ordena arranque básico, pero no garantiza que Qdrant ya acepte peticiones. Para sistemas serios se usan healthchecks o reintentos en la aplicación.

### Cómo leer un Compose de empresa

- Primero lista servicios.
- Después dibuja flechas por variables de entorno.
- Luego marca puertos expuestos al host.
- Por último marca volúmenes persistentes y secretos.

### Ejercicio de lectura

Coge cualquier `docker-compose.yml` y responde:

- [ ] ¿Qué servicios son infraestructura y cuáles son aplicación?
- [ ] ¿Qué servicio expone UI al navegador?
- [ ] ¿Qué servicio guarda datos?
- [ ] ¿Qué URL usaría un contenedor para llamar a otro?
- [ ] ¿Qué valores no deberían estar hardcodeados?

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
