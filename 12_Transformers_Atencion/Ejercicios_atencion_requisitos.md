# Ejercicios atención requisitos

## Ejercicio 1: desde cero

```bash
python 13_Labs/code/attention_requirements_from_scratch.py
```

Comprueba:

- [ ] Se imprime matriz A -> B.
- [ ] Se guarda `attention_a_to_b.png`.
- [ ] Se guarda `attention_b_to_a.png`.
- [ ] Las matrices no tienen la misma forma si A y B tienen distinto número de tokens.

## Ejercicio 2: transformer real

```bash
python 13_Labs/code/attention_requirements_with_transformers.py
```

Comprueba:

- [ ] Entiendes layers y heads.
- [ ] Se guarda CSV.
- [ ] Se guarda heatmap.
- [ ] Puedes explicar por qué no es explicación causal.

## Ejercicio 3: comparar

Compara:

- atención token-a-token
- cosine similarity entre embeddings globales
- BM25

Escribe cuándo usarías cada señal.

## Lección guiada

En atención entre requisitos, el objetivo es implementar y visualizar. No uses atención como veredicto; úsala como lupa.

### Preguntas

- ¿Quién aporta queries?
- ¿Quién aporta keys/values?
- ¿Qué forma tiene la matriz?
- ¿Por qué cada fila suma 1?
- ¿Por qué A -> B no equivale a B -> A?

### Práctica

```bash
python 13_Labs/code/attention_requirements_from_scratch.py
python 13_Labs/code/attention_requirements_with_transformers.py
```

### Evidencia

- [ ] Puedo derivar las dimensiones de Q, K, V.
- [ ] Puedo leer un heatmap.
- [ ] Puedo explicar por qué atención no es explicación causal.
