# Ejercicios RAG Requisitos

## Orden

1. `requirements_dataset.py`
2. `embedding_thresholds.py`
3. `bm25_hybrid.py`
4. levantar Qdrant
5. `qdrant_index_search.py`

## Comandos

```bash
python 13_Labs/code/requirements_dataset.py
python 13_Labs/code/embedding_thresholds.py
python 13_Labs/code/bm25_hybrid.py
docker run -p 6333:6333 -v qdrant_data:/qdrant/storage qdrant/qdrant:latest
python 13_Labs/code/qdrant_index_search.py
```

## Qué observar

- Embeddings recuperan semántica.
- BM25 recupera siglas/IDs.
- Hybrid mejora algunos casos y empeora otros.
- Qdrant no decide por ti: solo ejecuta búsqueda y filtros.

## Lección guiada

En retrieval, no te conformes con obtener resultados. Pregunta si son correctos, por qué aparecen y qué errores producen.

### Preguntas

- ¿La coincidencia es semántica, lexical o por metadata?
- ¿Qué pasaría si subo el threshold?
- ¿Qué candidato es falso positivo?
- ¿Qué relevante falta en top-k?
- ¿Qué filtro reduciría ruido?

### Práctica

```bash
python 13_Labs/code/embedding_thresholds.py
python 13_Labs/code/bm25_hybrid.py
python 13_Labs/code/qdrant_index_search.py
```

### Evidencia

- [ ] He comparado BM25 contra embeddings.
- [ ] He encontrado al menos un falso positivo.
- [ ] Sé explicar qué guarda Qdrant además del vector.
