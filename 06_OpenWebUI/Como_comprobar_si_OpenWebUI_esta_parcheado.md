# Cómo comprobar si OpenWebUI está parcheado

## Dentro del contenedor

```bash
docker compose exec openwebui sh
grep -R "hybrid_search" /app/backend/open_webui -n
grep -R "bm25" /app/backend/open_webui -n
grep -R "qdrant" /app/backend/open_webui -n
grep -R "text_enriched" /app/backend/open_webui -n
```

## En logs

```bash
docker compose logs -f openwebui
```

Busca líneas del script de arranque:

- patch encontrado
- patch aplicado
- versión base
- error de hunks

## Señales de sospecha

- El contenedor arranca pero no aparecen cambios esperados.
- `grep` no encuentra símbolos del patch.
- Aparecen `.rej` o errores de hunks.
- La imagen oficial cambió de tag sin actualizar patch.

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
