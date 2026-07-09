# Atención no es explicabilidad

La atención muestra pesos internos de un mecanismo concreto. Eso no garantiza que esos pesos sean una explicación causal de la decisión del modelo.

## Por qué tener cuidado

- Distintas heads pueden mirar cosas distintas.
- Layers tempranas y tardías tienen roles diferentes.
- Pesos altos no significan "razón verdadera".
- Un modelo puede cambiar salida sin cambios intuitivos en atención.
- En embeddings aleatorios, la atención no tiene semántica real.

## Uso correcto

Usa atención para inspeccionar relaciones entre requisitos, generar hipótesis y depurar. No la uses para aceptar cobertura, contradicción o equivalencia sin evaluación externa.

## Decisión responsable

Para decidir relación entre requisitos combina:

- golden set
- métricas retrieval
- revisión humana
- evidencia textual
- tests

## Ampliación curso: por qué esta advertencia importa en testing

En testing basado en requisitos, una explicación mala puede crear falsa trazabilidad. Si dices "este test cubre este requisito porque la atención mira a `DID`", estás confundiendo inspección con prueba.

### Diferencia entre evidencia y señal

- Atención: señal interna.
- BM25/embedding: señal de recuperación.
- Texto del requisito/test: evidencia.
- Ejecución del test: evidencia fuerte.
- Revisión humana: control de calidad.

### Uso responsable

La atención puede ayudarte a encontrar dónde mirar. Después debes justificar con texto:

> REQ-UDS-002 exige NRC 0x31 cuando DID no está soportado. TC-UDS-002 envía DID no soportado y espera NRC 0x31. Por tanto cubre el requisito.

Esa explicación es mejor que "la matriz de atención lo dijo".

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
