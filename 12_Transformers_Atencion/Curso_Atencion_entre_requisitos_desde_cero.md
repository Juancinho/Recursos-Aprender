# Curso atencion entre requisitos desde cero

## 1. Objetivo

Quieres pasar de saber teoria de Transformers a implementar una herramienta concreta:

```text
dado REQ_A y REQ_B, ver que tokens de A atienden a que tokens de B
```

Esto se parece a cross-attention:

- tokens de A producen queries;
- tokens de B producen keys y values;
- resultado: matriz `tokens_A x tokens_B`.

## 2. Formula

```text
Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V
```

Donde:

- `Q`: queries, lo que pregunta cada token;
- `K`: keys, contra que se compara;
- `V`: values, informacion que se mezcla;
- `d_k`: dimension de keys/queries;
- softmax por fila: cada token reparte atencion sobre los tokens del otro requisito.

## 3. Ejemplo

```text
REQ_A = "The ECU shall support UDS service 0x22 ReadDataByIdentifier."
REQ_B = "The diagnostic module shall return NRC 0x31 when the DID is unsupported."
```

Tokens simplificados:

```text
A: the, ecu, shall, support, uds, service, 0x22, readdatabyidentifier
B: the, diagnostic, module, shall, return, nrc, 0x31, when, the, did, is, unsupported
```

Si hacemos A -> B, cada fila es un token de A. Cada columna es un token de B.

## 4. Dimensiones

Supón:

```text
len(A)=8
len(B)=12
d_model=32
d_k=16
```

Entonces:

```text
X_A: 8 x 32
X_B: 12 x 32
W_Q: 32 x 16
W_K: 32 x 16
W_V: 32 x 16
Q_A = X_A W_Q: 8 x 16
K_B = X_B W_K: 12 x 16
V_B = X_B W_V: 12 x 16
scores = Q_A K_B^T: 8 x 12
attention_matrix: 8 x 12
output = attention_matrix V_B: 8 x 16
```

La matriz que visualizas es `8 x 12`.

## 5. Por que A -> B no es B -> A

A -> B pregunta:

```text
para representar tokens de A, que tokens de B uso?
```

B -> A pregunta:

```text
para representar tokens de B, que tokens de A uso?
```

Las matrices tienen formas distintas y pueden destacar relaciones distintas.

## 6. Diferencia con cosine global

Cosine global:

```text
REQ_A -> vector
REQ_B -> vector
cos(vector_A, vector_B)
```

Da una similitud total. No dice que token influyo.

Atencion token-a-token:

```text
token_A_i -> distribucion sobre tokens_B
```

Da una lupa local, pero no un veredicto fiable.

## 7. Diferencia con BM25

BM25 premia coincidencias exactas. Si ambos requisitos tienen `UDS`, `DID` o `NRC`, BM25 lo captura muy bien.

Atencion puede mostrar interaccion entre tokens aunque no sean identicos, pero depende de embeddings y pesos.

## 8. Atencion no es explicabilidad causal

Una cabeza de atencion alta no prueba que el modelo "razone por eso". Puede ser una correlacion interna, una consecuencia de entrenamiento o una distribucion dificil de interpretar.

Usala para inspeccionar:

- que tokens tecnicos se conectan;
- si el modelo mira IDs relevantes;
- si una relacion parece razonable.

No la uses sola para decidir:

- duplicado;
- contradiccion;
- cobertura;
- seguridad.

## 9. Practica

Desde cero:

```bash
python 13_Labs/code/attention_requirements_from_scratch.py
```

Con Transformers:

```bash
python 13_Labs/code/attention_requirements_with_transformers.py
```

Salidas esperadas:

- matriz como DataFrame;
- heatmap A -> B;
- heatmap B -> A;
- CSV si usas modelo real.

Para pasar de un par aislado a un grafo de requisitos, lee [[Grafo_de_requisitos_con_atencion]] y ejecuta:

```bash
python 13_Labs/code/requirements_attention_graph.py
```

La idea es generar candidatos primero y aplicar atencion solo a esos candidatos, guardando aristas con evidencia token-token.

## 10. Autocomprobacion

- [ ] Puedo escribir la formula sin mirar.
- [ ] Puedo derivar dimensiones de Q, K, V.
- [ ] Puedo explicar por que se divide por `sqrt(d_k)`.
- [ ] Puedo explicar por que cada fila suma 1.
- [ ] Puedo comparar atencion, BM25 y embeddings globales.
- [ ] Puedo explicar por que atencion no equivale a explicabilidad causal.
