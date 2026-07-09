# Qdrant

Qdrant es una base de datos vectorial. Guarda vectores y payloads asociados, permite búsqueda por similitud y filtros por metadata.

## Conceptos

- Collection: conjunto de points con la misma configuración vectorial.
- Point: registro con `id`, vector y payload.
- Payload: metadata como `module`, `requirement_id`, `source`, `version`.
- Filter: condición sobre payload.
- Dense vector: embedding denso.
- Sparse vector: representación dispersa para señales tipo BM25/SPLADE.

## Ejemplo de uso en requisitos

```json
{
  "id": "REQ-UDS-001",
  "vector": [0.12, -0.03, 0.44],
  "payload": {
    "module": "diagnostics",
    "text": "The ECU shall support UDS service 0x22 ReadDataByIdentifier."
  }
}
```

## Docker

```bash
docker run -p 6333:6333 -v qdrant_data:/qdrant/storage qdrant/qdrant:latest
```

Dashboard: `http://localhost:6333/dashboard`

## En OpenWebUI

OpenWebUI puede usar Qdrant como backend de vector DB para RAG. Debes mirar variables de entorno y configuración de retrieval.

## Ampliación curso: Qdrant como sistema de recuperación auditable

Qdrant no es solo "guardar embeddings". Para un proyecto serio necesitas que cada resultado sea auditable: de dónde viene, qué versión tiene, qué módulo, qué texto original y qué transformación recibió.

### Diseño de colección para requisitos

```json
{
  "collection": "requirements",
  "vector_size": 384,
  "distance": "Cosine",
  "payload_schema": {
    "requirement_id": "keyword",
    "module": "keyword",
    "source": "keyword",
    "version": "keyword",
    "text": "text",
    "status": "keyword"
  }
}
```

### Payload mínimo responsable

- `requirement_id`: para trazabilidad.
- `module`: para filtros.
- `text`: para mostrar evidencia.
- `source`: documento o archivo origen.
- `version`: versión de especificación.
- `hash`: para detectar cambios de texto.

### Fallos frecuentes

- Cambiar modelo de embeddings sin recrear colección.
- Mezclar dimensiones distintas.
- No guardar texto original.
- No filtrar por módulo.
- Borrar contenedor y perder datos por no usar volumen.

### Checklist de producción

- [ ] Sé qué modelo creó los vectores.
- [ ] Sé dimensión y distancia.
- [ ] Sé cómo reindexar.
- [ ] Sé cómo filtrar por metadata.
- [ ] Sé cómo reproducir una búsqueda.

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
