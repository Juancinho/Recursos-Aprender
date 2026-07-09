# Atención entre dos requisitos

Queremos comparar dos requisitos independientes token a token.

REQ_A = "The ECU shall support UDS service 0x22 ReadDataByIdentifier."

REQ_B = "The diagnostic module shall return NRC 0x31 when the DID is unsupported."

## Objetivo

Construir una matriz `token_A x token_B` donde cada fila indica cuánto atiende un token de A a los tokens de B.

## Procedimiento

1. Tokenizar A y B.
2. Crear embeddings de tokens.
3. Crear matrices `W_Q`, `W_K`, `W_V`.
4. Calcular `Q_A = X_A W_Q`.
5. Calcular `K_B = X_B W_K`.
6. Calcular `V_B = X_B W_V`.
7. Calcular `scores = Q_A K_B^T / sqrt(d_k)`.
8. Aplicar softmax por filas.
9. Obtener matriz de atención.
10. Visualizar heatmap.
11. Repetir B -> A.

## Interpretación

Si una fila concentra peso en `DID` o `NRC`, ese token de A está usando información de esos tokens de B dentro de esta parametrización. Pero no concluyas causalidad ni verdad funcional.

## Comparación con otros métodos

- Embeddings globales: un vector por requisito; buena señal global, poca inspección token-a-token.
- BM25: coincidencias léxicas; fuerte para `UDS`, `0x22`, `NRC`.
- Atención: inspección local token-a-token; útil para análisis, no decisión automática.

> [!warning]
> Atención no equivale automáticamente a explicación fiable. Ver [[Atencion_no_es_explicabilidad]].

## De pares a grafo

Cuando tienes muchos requisitos, por ejemplo 800, no haces atencion detallada entre todos los pares. Primero generas candidatos con [[Embeddings_para_requisitos]], [[BM25]], [[Hybrid_Search]] o [[Qdrant]]. Despues aplicas atencion cruzada solo a esos pares candidatos para construir aristas con peso y evidencia.

La nota practica es [[Grafo_de_requisitos_con_atencion]] y el lab asociado es [[Lab_14_Grafo_Requisitos_Atencion]].

## Ampliación curso: atención como herramienta de inspección de relaciones

### Qué quieres inspeccionar

Dos requisitos pueden estar relacionados de varias formas:

- mismo servicio UDS;
- mismo DID;
- condición complementaria;
- caso positivo vs negativo;
- contradicción;
- mismo módulo pero distinta función.

La atención token-a-token puede ayudarte a ver qué tokens técnicos interactúan, pero no decide la etiqueta.

### A -> B

A pregunta: "para representar cada token de A, qué tokens de B uso".

Esto es útil si A es la query principal y B es candidato recuperado.

### B -> A

B pregunta lo inverso. Puede resaltar otros tokens. Por ejemplo, B puede centrarse en `NRC` y `DID`, mientras A se centra en `UDS` y `0x22`.

### Comparación práctica

| Método | Unidad | Bueno para | Malo para |
|---|---|---|---|
| Cosine global | requisito completo | ranking rápido | explicar tokens concretos |
| BM25 | términos | IDs/siglas exactas | paráfrasis |
| Atención | tokens | inspección local | decisión fiable sin evaluación |

### Informe recomendado

Para cada par de requisitos dudoso escribe:

- similitud embedding;
- score BM25;
- tokens con mayor atención A -> B;
- tokens con mayor atención B -> A;
- decisión humana;
- razón.

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
