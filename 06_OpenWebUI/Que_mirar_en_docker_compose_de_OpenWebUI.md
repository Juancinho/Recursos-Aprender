# Qué mirar en docker-compose de OpenWebUI

- [ ] Imagen exacta y tag.
- [ ] `command` o `entrypoint`.
- [ ] Volúmenes montados.
- [ ] Archivo patch montado.
- [ ] Variables de entorno de modelos.
- [ ] Variables de Qdrant.
- [ ] Puerto publicado.
- [ ] Dependencias (`depends_on`).
- [ ] Healthchecks.
- [ ] Redes.

## Preguntas

- ¿OpenWebUI llama directamente a vLLM o pasa por LiteLLM?
- ¿Qdrant está en la misma red Compose?
- ¿Dónde se guardan datos persistentes?
- ¿El patch se aplica siempre o solo si detecta una versión?

## Lección guiada

En OpenWebUI, separa interfaz, backend, retrieval, configuración y modelo. Cuando algo falla, ubica primero en qué tramo está el fallo.

### Preguntas

- ¿OpenWebUI llama al modelo directamente o vía LiteLLM?
- ¿Dónde está configurado Qdrant?
- ¿El patch se aplicó realmente?
- ¿Qué logs muestran retrieval?
- ¿Qué grep confirma símbolos propios?

### Práctica

```bash
docker compose logs -f openwebui
grep -R "hybrid_search" /app/backend/open_webui -n
grep -R "bm25" /app/backend/open_webui -n
grep -R "qdrant" /app/backend/open_webui -n
```

### Evidencia

- [ ] Puedo dibujar OpenWebUI -> Qdrant -> modelo.
- [ ] Puedo explicar imagen oficial + patch.
- [ ] Puedo hacer una checklist de inspección.
