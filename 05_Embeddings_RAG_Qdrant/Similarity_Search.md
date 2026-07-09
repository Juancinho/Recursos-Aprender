# Similarity Search

Búsqueda de similitud: dada una query, recuperar documentos cercanos según una función de distancia o similitud.

## Conecta con
- [[Embeddings_para_requisitos]]
- [[Thresholds_Falsos_Positivos_Falsos_Negativos]]

## Coseno
`cos(a,b) = dot(a,b)/(||a|| ||b||)`.

## Top-k
Top-5 puede ser útil para revisión humana; top-1 suele ser frágil.

## Interpretación
Similitud alta no significa relación correcta. Significa candidato.

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
