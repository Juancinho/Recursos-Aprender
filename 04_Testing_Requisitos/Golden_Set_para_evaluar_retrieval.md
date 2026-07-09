# Golden Set para evaluar retrieval

Un golden set es un conjunto pequeño pero revisado manualmente con respuestas correctas. Sirve para evaluar si embeddings, BM25 o hybrid search recuperan lo que deben.

## Conecta con
- [[Evaluacion_Retrieval]]
- [[Hybrid_Search]]

## Formato
`query_id`, `relevant_requirement_id`, `relevance` donde relevance puede ser 0/1 o 0/1/2.

## Uso
Calcula precision@k, recall@k, MRR y NDCG. Ajusta thresholds sin mirar solo ejemplos bonitos.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Ampliación curso: diseñar un golden set que no engañe

Un golden set pequeño puede ser peor que nada si solo contiene casos fáciles. Debe incluir casos positivos, negativos y difíciles.

### Tipos de ejemplos necesarios

- Positivos obvios: mismo DID, mismo servicio.
- Positivos parafraseados: diferente vocabulario, misma obligación.
- Negativos parecidos: comparten palabras pero no relación.
- Contradicciones: parecen relacionados pero chocan.
- Módulos cruzados: palabras comunes en dominios distintos.
- IDs exactos: `0x22`, `0x31`, CAN IDs.

### Formato recomendado

```csv
query_id,candidate_id,relevance,reason
REQ-UDS-001,TC-UDS-001,2,"same service and positive response"
REQ-UDS-001,TC-LGT-001,0,"different module"
REQ-UDS-002,REQ-UDS-001,1,"related UDS service but different expected behavior"
```

### Relevance graduada

- `0`: no relevante.
- `1`: relacionado, útil como contexto pero no cobertura directa.
- `2`: relevante/cubre directamente.

### Regla de oro

> [!warning]
> No ajustes thresholds mirando solo los aciertos. Guarda y revisa los errores; ahí está el aprendizaje.

## Lección guiada

En testing basado en requisitos, convierte frases en estructuras verificables. Busca actor, acción, condición, resultado esperado y evidencia.

### Preguntas

- ¿Qué se debe comprobar?
- ¿En qué condición?
- ¿Qué respuesta sería correcta?
- ¿Qué test lo cubre?
- ¿Qué sería un falso match?

### Práctica

```bash
python 13_Labs/code/requirements_dataset.py
python 13_Labs/code/coverage_checker.py
```

### Evidencia

- [ ] Puedo separar requisito, test y evidencia.
- [ ] Puedo detectar un gap.
- [ ] Puedo explicar una relación de trazabilidad.
