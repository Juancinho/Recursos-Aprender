# Puertos, Volúmenes y Redes

Tres fuentes habituales de problemas: no entender qué puerto vive dentro del contenedor, perder datos por no usar volúmenes y no saber cómo se resuelven nombres entre servicios.

## Conecta con
- [[Docker]]
- [[Docker_Compose]]
- [[OpenWebUI_con_Qdrant]]

## Puertos
`HOST:CONTENEDOR`. En `6333:6333`, tu navegador usa `localhost:6333` y Qdrant escucha dentro en `6333`.

## Volúmenes
Persisten datos. Para Qdrant, un volumen evita perder colecciones al recrear el contenedor.

## Redes
En Compose, `openwebui` puede llamar a `http://qdrant:6333` si ambos servicios comparten red.

## Comandos
```bash
docker volume ls
docker network ls
docker inspect <container>
```

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

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
