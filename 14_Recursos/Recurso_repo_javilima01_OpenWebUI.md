# Recurso repo javilima01 OpenWebUI

## Enlace

- https://github.com/javilima01/open-webui

## Por qué es importante

Es el repo que mencionaste como referencia del patch que aplica la empresa sobre OpenWebUI. Debe estudiarse junto a:

- [[Repo_javilima01_OpenWebUI]]
- [[Analisis_codigo_hybrid_search_javilima01]]
- [[Como_convertir_repo_javilima01_en_patch_empresa]]
- [[OpenWebUI_imagen_oficial_mas_patch]]

## Qué mirar

- `backend/open_webui/retrieval/utils.py`
- `backend/open_webui/config.py`
- `backend/open_webui/routers/retrieval.py`
- `backend/open_webui/utils/middleware.py`
- `backend/open_webui/retrieval/vector/dbs/qdrant.py`
- `src/lib/components/admin/Settings/Documents.svelte`
- `pyproject.toml`
- `backend/requirements.txt`

## Preguntas de lectura

- [ ] ¿Qué cambios son de hybrid search?
- [ ] ¿Qué cambios son de Qdrant?
- [ ] ¿Qué cambios son de embeddings?
- [ ] ¿Qué cambios son solo versión upstream?
- [ ] ¿Qué cambio es imprescindible para el patch de empresa?
- [ ] ¿Qué cambio es UI y qué cambio es backend?

## Comandos útiles

```bash
rg -n "hybrid|BM25|qdrant|RAG_HYBRID|ENABLE_RAG_HYBRID" _repos/open-webui-javilima01/backend _repos/open-webui-javilima01/src
rg -n "query_doc_with_hybrid_search|query_collection_with_hybrid_search|VectorSearchRetriever" _repos/open-webui-javilima01/backend
rg -n "RAG_HYBRID_BM25_WEIGHT|ENABLE_RAG_HYBRID_SEARCH" _repos/open-webui-javilima01/backend/open_webui/config.py
```

## Entregable

Después de estudiar este recurso, deberías poder explicar en 5 minutos:

1. qué añade el fork respecto a retrieval;
2. cómo se activa desde configuración;
3. dónde está la UI;
4. dónde se llama desde el chat;
5. qué hace Qdrant;
6. qué necesitas saber para generar el patch real.

