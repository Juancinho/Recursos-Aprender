# Testing basado en requisitos

Un requisito describe una capacidad, restricción o comportamiento esperado. Un test case verifica algo observable. La trazabilidad conecta ambos.

## Vocabulario

- Requirement: "The ECU shall support UDS service 0x22".
- Specification: documento más amplio, con contexto, interfaces y restricciones.
- Test case: procedimiento verificable con pasos y resultado esperado.
- Traceability: relación requisito -> test.
- Coverage: porcentaje o conjunto de requisitos cubiertos.
- Gap: requisito sin test.
- Duplicado: dos requisitos dicen casi lo mismo.
- Contradicción: dos requisitos no pueden cumplirse a la vez.
- Ambiguo: usa términos no medibles como "rápido" o "adecuado".
- Verificación: construimos bien el producto.
- Validación: construimos el producto correcto.
- Regression testing: comprobar que cambios nuevos no rompen lo anterior.
- Golden set: conjunto etiquetado manualmente para evaluar retrieval o matching.

## Ejemplo

| id | module | requirement |
|---|---|---|
| REQ-UDS-001 | diagnostics | The ECU shall support UDS service 0x22 ReadDataByIdentifier. |
| REQ-LGT-001 | lighting | The vehicle shall turn on low beam when ambient light is below threshold. |

| test_id | covers | expected |
|---|---|---|
| TC-UDS-001 | REQ-UDS-001 | Positive response contains DID data. |

## Señales útiles para IA

Un sistema de IA puede sugerir tests relacionados, gaps o duplicados, pero necesita evaluación. La métrica no es "suena bien"; es si recupera relaciones correctas en el [[Golden_Set_para_evaluar_retrieval]].

## Ampliación curso: de texto natural a verificación

Un requisito útil para testing debe poder transformarse en una pregunta verificable.

### Anatomía de un requisito

Ejemplo:

> The ECU shall return NRC 0x31 when the DID is unsupported.

Separación:

- Actor/sistema: ECU.
- Obligación: shall return.
- Resultado: NRC 0x31.
- Condición: when the DID is unsupported.
- Dominio: UDS/diagnostics.

Test derivado:

- Precondición: ECU en sesión diagnóstica válida.
- Estímulo: request `0x22` con DID no soportado.
- Esperado: negative response con NRC `0x31`.
- Evidencia: traza CAN/DoIP o log del tester.

### Tipos de mala calidad en requisitos

| Problema | Ejemplo | Por qué duele |
|---|---|---|
| Ambigüedad | "respond quickly" | no hay threshold |
| Falta condición | "shall return error" | no dice cuándo |
| Duplicado | dos textos equivalentes | infla coverage |
| Contradicción | positive response y NRC para mismo caso | imposible verificar |
| Mezcla | dos obligaciones en una frase | test difícil de trazar |

### Cómo ayuda IA

La IA puede:

- proponer tests candidatos;
- detectar requisitos parecidos;
- agrupar por módulo;
- sugerir gaps;
- extraer condiciones y expected results.

Pero debe evaluarse con un golden set. Si no, puede crear falsa confianza.

### Ejercicio profundo

Toma 10 requisitos. Para cada uno:

- [ ] Extrae actor, acción, condición y resultado.
- [ ] Escribe un test manual.
- [ ] Marca si es ambiguo.
- [ ] Busca duplicados por BM25.
- [ ] Busca parecidos por embeddings.
- [ ] Decide si la sugerencia automática es correcta.

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
