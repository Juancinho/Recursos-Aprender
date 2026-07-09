# Docker para OpenWebUI, Qdrant y LiteLLM

Estos servicios suelen desplegarse juntos: OpenWebUI como interfaz, Qdrant como vector DB, LiteLLM como gateway y vLLM como servidor local de modelos.

## Conecta con
- [[OpenWebUI]]
- [[Qdrant]]
- [[LiteLLM]]
- [[vLLM]]

## Compose mental
OpenWebUI necesita URL de Qdrant y endpoint OpenAI-compatible. LiteLLM puede ocultar si detrás está vLLM, OpenAI, Azure u otro proveedor.

## Variables típicas
`QDRANT_URI`, `OPENAI_API_BASE_URL`, `OPENAI_API_KEY`, `LITELLM_MASTER_KEY`, `WEBUI_SECRET_KEY`.

## Inspección
```bash
docker compose ps
docker compose logs -f openwebui
docker compose exec openwebui sh
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
