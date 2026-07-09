# Imagen vs Contenedor

Una imagen Docker es una plantilla; un contenedor es una instancia ejecutándose. La imagen no cambia cuando el contenedor escribe datos, salvo que construyas una nueva imagen.

## Conecta con
- [[Docker]]
- [[Docker_Compose]]

## Analogía útil
Imagen = clase o snapshot. Contenedor = proceso/instancia. Puedes crear muchos contenedores desde la misma imagen.

## Comandos
```bash
docker images
docker run --name demo-nginx -d nginx:alpine
docker ps
docker stop demo-nginx
docker rm demo-nginx
```

## En Technica
OpenWebUI puede venir de una imagen oficial. El contenedor resultante puede recibir un patch al arrancar, pero eso no modifica la imagen oficial original.

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
