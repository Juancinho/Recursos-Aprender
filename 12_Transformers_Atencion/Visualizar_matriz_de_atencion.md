# Visualizar matriz de atención

Una matriz de atención para A -> B tiene forma:

`n_tokens_A x n_tokens_B`

Cada fila suma 1 si aplicas softmax por filas.

## Heatmap

- Eje Y: tokens query, por ejemplo tokens de A.
- Eje X: tokens key, por ejemplo tokens de B.
- Color: peso de atención.

## Qué mirar

- Filas muy concentradas.
- Tokens técnicos: `UDS`, `0x22`, `NRC`, `DID`.
- Diferencias A -> B y B -> A.
- Cabezas/layers si usas un transformer real.

## Scripts

```bash
python 13_Labs/code/attention_requirements_from_scratch.py
python 13_Labs/code/attention_requirements_with_transformers.py
```

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
