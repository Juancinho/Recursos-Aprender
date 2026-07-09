# OpenWebUI

OpenWebUI es una interfaz web para interactuar con modelos y flujos de chat/RAG. En un proyecto empresarial puede actuar como punto de entrada para usuarios internos, testing asistido y consultas sobre documentación.

## Alto nivel

- Frontend: interfaz de chat/configuración.
- Backend: APIs, autenticación, integración con modelos y RAG.
- RAG: ingesta, embeddings, vector DB, retrieval y contexto.
- Model provider: puede ser OpenAI, LiteLLM, vLLM u otro endpoint compatible.

## En este proyecto

La información que te dieron sugiere:

- Imagen Docker oficial.
- Patch/diff propio al arrancar.
- Qdrant para vector search.
- Posibles cambios sobre BM25/hybrid/text enrichment.
- LLM local Qwen servido vía vLLM y/o LiteLLM.

## Comandos de inspección

```bash
docker compose logs -f openwebui
docker compose exec openwebui sh
grep -R "hybrid_search" /app/backend/open_webui -n
grep -R "bm25" /app/backend/open_webui -n
grep -R "qdrant" /app/backend/open_webui -n
```

## Ampliación curso: cómo pensar OpenWebUI sin leer todo el código

OpenWebUI es el punto donde se juntan usuario, configuración, documentos, retrieval y modelos. Para entenderlo, sepáralo en rutas de flujo:

### Flujo de chat sin RAG

Usuario escribe -> backend recibe mensaje -> backend llama endpoint de modelo -> streaming de tokens -> UI muestra respuesta.

### Flujo con RAG

Usuario escribe -> backend busca documentos relevantes -> construye prompt con contexto -> llama modelo -> UI muestra respuesta con contexto.

### Flujo con patch propio

Contenedor arranca -> entrypoint aplica patch -> backend queda modificado -> OpenWebUI usa funcionalidad propia como hybrid search, BM25 o payload enriquecido.

### Qué debes localizar en un repo OpenWebUI modificado

- Dónde se configuran proveedores de modelos.
- Dónde se decide vector DB.
- Dónde se crean embeddings.
- Dónde se llama a Qdrant.
- Dónde se hace reranking/hybrid.
- Dónde se guardan documentos.
- Dónde aparecen logs de errores.

### Preguntas útiles para la empresa

- [ ] ¿Qué versión oficial de OpenWebUI se usa?
- [ ] ¿Qué patch interno se aplica?
- [ ] ¿El patch está testeado?
- [ ] ¿Qdrant sustituye a otro vector DB o convive?
- [ ] ¿BM25 está dentro de OpenWebUI o en servicio aparte?
- [ ] ¿El usuario puede configurar top-k/threshold?

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

## Repo específico de tu jefe

Añadido para el caso de Technica:

- [[Repo_javilima01_OpenWebUI]]
- [[Analisis_codigo_hybrid_search_javilima01]]
- [[Como_convertir_repo_javilima01_en_patch_empresa]]

Este repo es importante porque contiene el código que probablemente se convierte en diff/patch aplicado sobre la imagen oficial de OpenWebUI. No lo estudies como "OpenWebUI entero"; estúdialo por rutas: configuración RAG, retrieval, Qdrant, UI admin y middleware.
