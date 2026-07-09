# Thresholds, Falsos Positivos y Falsos Negativos

El threshold decide qué candidatos aceptas automáticamente o mandas a revisión. Moverlo cambia el tipo de error.

## Conecta con
- [[Embeddings_para_requisitos]]
- [[Evaluacion_Retrieval]]

## Falso positivo
Aceptas relación que no existe. En testing puede crear falsa cobertura.

## Falso negativo
Pierdes relación real. En testing puede parecer que hay gap donde sí había cobertura.

## Práctica
Evalúa thresholds 0.5, 0.6, 0.7, 0.8, 0.9 con `embedding_thresholds.py`.

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
