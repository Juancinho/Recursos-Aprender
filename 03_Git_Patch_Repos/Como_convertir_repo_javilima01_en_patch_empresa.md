# Cómo convertir repo javilima01 en patch de empresa

Esta nota explica cómo razonar sobre el caso que te contaron:

> Imagen Docker oficial de OpenWebUI + diff/patch con cambios del repo de tu jefe.

Repo de tu jefe:

- https://github.com/javilima01/open-webui
- clon local: `_repos/open-webui-javilima01`

## Idea central

Un patch útil no se genera contra "OpenWebUI actual" de forma genérica. Se genera contra una base exacta:

- tag;
- commit;
- digest de imagen Docker;
- rama concreta.

Si no sabes la base exacta, cualquier diff puede mezclar cambios reales de empresa, cambios normales de versión upstream, archivos generados y cambios de formato no relacionados.

## Lo que hice localmente

Cloné:

```bash
git clone --depth 1 https://github.com/javilima01/open-webui.git _repos/open-webui-javilima01
git clone --depth 1 https://github.com/open-webui/open-webui.git _repos/open-webui-upstream
```

Después comparé rutas relevantes. La comparación contra upstream actual sale muy grande y no sirve como patch limpio porque las bases no están alineadas.

> [!warning]
> No concluyas que todo el diff contra upstream actual es "el patch de tu jefe". Primero hay que conocer la base oficial exacta.

## Procedimiento correcto

### 1. Preguntar base exacta

- [ ] ¿Qué imagen oficial usan? Ejemplo: `ghcr.io/open-webui/open-webui:main`, `v0.x.y`, digest SHA.
- [ ] ¿Qué commit/tag de OpenWebUI corresponde a esa imagen?
- [ ] ¿Qué commit del repo `javilima01/open-webui` contiene los cambios?
- [ ] ¿El patch se aplica con `git apply`, `patch`, `cp` o script propio?

### 2. Clonar base y versión modificada

```bash
git clone https://github.com/open-webui/open-webui.git open-webui-base
cd open-webui-base
git checkout <commit_base_oficial>
```

```bash
git clone https://github.com/javilima01/open-webui.git open-webui-javilima
cd open-webui-javilima
git checkout <commit_modificado>
```

### 3. Generar diff por rutas, no a ciegas

```bash
git diff --no-index open-webui-base/backend/open_webui/retrieval/utils.py open-webui-javilima/backend/open_webui/retrieval/utils.py
git diff --no-index open-webui-base/backend/open_webui/config.py open-webui-javilima/backend/open_webui/config.py
git diff --no-index open-webui-base/backend/open_webui/routers/retrieval.py open-webui-javilima/backend/open_webui/routers/retrieval.py
git diff --no-index open-webui-base/src/lib/components/admin/Settings/Documents.svelte open-webui-javilima/src/lib/components/admin/Settings/Documents.svelte
```

### 4. Crear patch limpio

Si las bases están bien alineadas:

```bash
git diff <commit_base>..<commit_modificado> > technica-openwebui.patch
```

### 5. Probar patch

```bash
cd open-webui-base
git apply --check ../technica-openwebui.patch
git apply ../technica-openwebui.patch
```

### 6. Verificación funcional

```bash
rg -n "ENABLE_RAG_HYBRID_SEARCH|RAG_HYBRID_BM25_WEIGHT|ENABLE_RAG_HYBRID_SEARCH_ENRICHED_TEXTS" backend src
rg -n "query_doc_with_hybrid_search|BM25Retriever|EnsembleRetriever" backend
rg -n "qdrant|QDRANT_URI|VECTOR_DB" backend
```

Y en contenedor:

```bash
docker compose logs -f open-webui
docker compose exec open-webui sh
grep -R "hybrid_search" /app/backend/open_webui -n
grep -R "bm25" /app/backend/open_webui -n
grep -R "qdrant" /app/backend/open_webui -n
```

## Archivos probablemente centrales del patch

Según el análisis local:

- `backend/open_webui/config.py`
- `backend/open_webui/main.py`
- `backend/open_webui/retrieval/utils.py`
- `backend/open_webui/routers/retrieval.py`
- `backend/open_webui/utils/middleware.py`
- `backend/open_webui/retrieval/vector/dbs/qdrant.py`
- `backend/requirements.txt`
- `pyproject.toml`
- `src/lib/components/admin/Settings/Documents.svelte`

## Qué documentar por cada hunk

| Campo | Pregunta |
|---|---|
| Archivo | ¿Dónde está? |
| Propósito | ¿Qué comportamiento cambia? |
| Riesgo | ¿Qué puede romper? |
| Config | ¿Qué variable lo activa? |
| Prueba | ¿Cómo sé que funciona? |
| Fallback | ¿Qué pasa si falla? |

## Ejercicio

- [ ] Pregunta o localiza el tag oficial base.
- [ ] Genera diff solo de `retrieval/utils.py`.
- [ ] Marca hunks de hybrid search.
- [ ] Escribe un resumen de cada hunk.
- [ ] Prueba `git apply --check`.
- [ ] Añade comprobaciones grep al script de arranque.

