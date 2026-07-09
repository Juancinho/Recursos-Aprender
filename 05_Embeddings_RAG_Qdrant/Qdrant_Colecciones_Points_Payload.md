# Qdrant Colecciones, Points y Payload

La colección define cómo son los vectores. Los points contienen vector + payload. El payload permite filtrar y explicar resultados.

## Conecta con
- [[Qdrant]]
- [[Qdrant_Filtros_Metadata]]

## Collection
Ejemplo: `requirements` con dimensión 384 y distancia cosine.

## Point
`id`, `vector`, `payload`.

## Payload recomendado
`requirement_id`, `module`, `text`, `source_file`, `version`, `status`.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

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
