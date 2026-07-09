# Errores Comunes Docker

La mayor parte de errores Docker al empezar no son de IA: son puertos ocupados, contenedores cerrados, variables mal puestas o rutas de Windows.

## Conecta con
- [[Docker]]
- [[Docker_Compose]]

## Puerto ocupado
Cambia `8080:80` a `8081:80` o identifica el proceso que usa el puerto.

## Contenedor se apaga
Mira `docker logs <container>`. Si el proceso principal termina, el contenedor termina.

## Permisos/volúmenes
Evita rutas raras de Windows al inicio. Usa volúmenes nombrados cuando puedas.

## CRLF
Scripts `.sh` con finales Windows pueden fallar con errores tipo `not found` aunque el archivo exista.

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
