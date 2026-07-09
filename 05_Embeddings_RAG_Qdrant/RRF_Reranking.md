# RRF y Reranking

RRF combina rankings dando más peso a posiciones altas. Reranking reordena candidatos con un modelo más caro o una regla más precisa.

## Conecta con
- [[Hybrid_Search]]
- [[Evaluacion_Retrieval]]

## RRF
`score(d)=sum(1/(k+rank_i(d)))`.

## Uso
Recupera 50 candidatos con BM25+dense y rerankea top 10.

## Riesgo
Reranking no arregla candidatos que nunca recuperaste.

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
