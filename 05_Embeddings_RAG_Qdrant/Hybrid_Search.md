# Hybrid Search

Hybrid search combina señales densas y sparse. En requisitos suele ser útil porque conviven semántica, siglas, IDs y condiciones exactas.

## Conecta con
- [[BM25]]
- [[Embeddings_para_requisitos]]
- [[RRF_Reranking]]

## Combinación por alpha
`score = alpha * dense + (1-alpha) * bm25_normalizado`.

## RRF
Reciprocal Rank Fusion combina rankings sin exigir scores comparables.

## Consejo
No elijas alpha por intuición: pruébalo contra un golden set.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Ampliación curso: diseño de búsqueda híbrida

Hybrid search no significa "sumar dos scores y ya". Hay tres problemas:

1. Los scores de BM25 y dense no tienen la misma escala.
2. Los rankings pueden contradecirse.
3. La mejor mezcla depende del dominio y del golden set.

### Estrategias

#### Normalización + alpha

```text
score = alpha * dense_norm + (1 - alpha) * bm25_norm
```

Útil para entender, pero sensible a normalización.

#### RRF

Combina posiciones, no scores. Suele ser robusto cuando los scores no son comparables.

#### Reranking

Recuperas candidatos con BM25+dense y luego un modelo más caro decide orden final.

### En requisitos

- Usa BM25 para IDs, siglas y nombres exactos.
- Usa dense para paráfrasis.
- Usa filtros Qdrant para módulo, versión o fuente.
- Usa revisión humana para relaciones dudosas.

### Preguntas de diseño

- [ ] ¿Quiero maximizar recall para revisión humana?
- [ ] ¿Quiero precisión alta para automatizar?
- [ ] ¿Qué hago con candidatos de módulos distintos?
- [ ] ¿Cómo trato contradicciones?

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
