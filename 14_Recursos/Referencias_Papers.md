# Referencias papers

## Lecturas obligatorias y para qué sirven

### Attention Is All You Need

- URL: https://arxiv.org/abs/1706.03762
- Úsalo para: entender scaled dot-product attention, multi-head attention y la arquitectura Transformer original.
- Conecta con: [[Atencion_desde_cero]], [[Self_Attention_vs_Cross_Attention]], [[Atencion_entre_dos_requisitos]].
- Qué leer primero: resumen, sección 3.2, figura de arquitectura.

### Efficient Memory Management for Large Language Model Serving with PagedAttention

- URL: https://arxiv.org/abs/2309.06180
- Úsalo para: entender por qué vLLM existe y por qué KV cache domina serving.
- Conecta con: [[vLLM]], [[KV_Cache_Batching_Streaming]], [[Motor_de_inferencia]].
- Qué leer primero: problema de fragmentación de KV cache y explicación de PagedAttention.

### Introduction to Information Retrieval

- URL: https://nlp.stanford.edu/IR-book/
- Úsalo para: BM25, ranking, evaluación, precision/recall.
- Conecta con: [[BM25]], [[Evaluacion_Retrieval]], [[Golden_Set_para_evaluar_retrieval]].
- Qué leer primero: capítulos de scoring, evaluation y relevance feedback.

## Cómo leer papers sin ahogarte

1. Lee abstract.
2. Mira figuras.
3. Lee problema, no detalles matemáticos todavía.
4. Busca qué limitación resuelve.
5. Escribe una explicación de 5 líneas conectada al proyecto.

> [!todo]
> No intentes entender cada demostración. Tu objetivo inicial es saber qué idea técnica cambia tu manera de depurar o diseñar.
