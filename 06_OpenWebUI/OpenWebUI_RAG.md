# OpenWebUI RAG

RAG añade documentos recuperados como contexto para el modelo. La calidad depende de chunking, embeddings, retrieval, reranking y prompts.

## Conecta con
- [[OpenWebUI]]
- [[Qdrant]]
- [[Hybrid_Search]]

## Pipeline
Ingesta -> chunking -> embeddings -> Qdrant -> consulta -> top-k -> prompt -> respuesta.

## Errores
Chunks malos, thresholds malos, metadatos pobres, top-k excesivo o prompt que no fuerza citar contexto.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

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
