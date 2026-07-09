# Atención desde cero

La atención scaled dot-product calcula cuánto atiende cada query a cada key y usa esos pesos para combinar values.

## Fórmula

`Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V`

## Piezas

- Q: queries, lo que busca cada token.
- K: keys, contra qué se compara.
- V: values, información que se mezcla.
- `d_k`: dimensión de las keys.
- softmax: convierte scores por fila en distribución de pesos.

## Pasos

1. Tokens -> embeddings.
2. Multiplicar por matrices aprendidas `W_Q`, `W_K`, `W_V`.
3. Calcular `scores = QK^T / sqrt(d_k)`.
4. Aplicar softmax por filas.
5. Multiplicar por `V`.

## Didáctico vs real

El script [[Lab_11_Atencion_Requisitos]] desde cero usa embeddings aleatorios reproducibles. Sirve para entender formas matriciales, no semántica real.

## Ampliación curso: formas matriciales

Supón:

- secuencia A tiene `n_a` tokens;
- secuencia B tiene `n_b` tokens;
- dimensión de embedding `d_model`;
- dimensión de key/query `d_k`.

Entonces:

```text
X_A: n_a x d_model
X_B: n_b x d_model
W_Q: d_model x d_k
W_K: d_model x d_k
W_V: d_model x d_v

Q_A = X_A W_Q: n_a x d_k
K_B = X_B W_K: n_b x d_k
V_B = X_B W_V: n_b x d_v

scores = Q_A K_B^T: n_a x n_b
weights = softmax(scores / sqrt(d_k)): n_a x n_b
output = weights V_B: n_a x d_v
```

### Por qué dividir por `sqrt(d_k)`

Si `d_k` crece, los productos punto tienden a tener magnitudes mayores. Softmax se saturaría y produciría distribuciones demasiado picudas. La escala estabiliza.

### Qué significa una fila

Una fila corresponde a un token query. Sus pesos sobre columnas indican cómo reparte atención sobre tokens key.

### Ejemplo con requisitos

En A -> B:

- filas: tokens de "The ECU shall support UDS service 0x22..."
- columnas: tokens de "The diagnostic module shall return NRC 0x31..."

Si la fila `UDS` mira a `diagnostic`, `DID` o `NRC`, puede indicar relación interna del modelo entre esos tokens. En el script desde cero, como los embeddings son aleatorios, solo estudias el mecanismo.

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
