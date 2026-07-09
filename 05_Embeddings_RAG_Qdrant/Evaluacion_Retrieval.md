# Evaluación Retrieval

## Métricas

- Precision@k: de los k recuperados, cuántos son relevantes.
- Recall@k: de los relevantes existentes, cuántos recuperaste.
- MRR: premia que el primer relevante aparezca pronto.
- NDCG: premia ranking correcto con relevancia graduada.

## Ejemplo

Si para una query hay 2 requisitos relevantes y tu top-5 contiene 1 relevante:

- recall@5 = 1/2
- precision@5 = 1/5

## Uso práctico

1. Construye [[Golden_Set_para_evaluar_retrieval]].
2. Ejecuta embeddings.
3. Ejecuta BM25.
4. Ejecuta hybrid.
5. Compara métricas y errores cualitativos.

> [!warning]
> No optimices solo un ejemplo. Mira errores repetidos: siglas, negaciones, módulos, IDs, requisitos largos.

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
