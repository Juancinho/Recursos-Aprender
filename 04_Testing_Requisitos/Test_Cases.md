# Test Cases

Un test case debe ser observable, repetible y vinculado a un requisito. Si no se puede ejecutar o revisar, no sirve para coverage real.

## Conecta con
- [[Testing_basado_en_requisitos]]
- [[Trazabilidad]]

## Campos
`test_id`, `title`, `preconditions`, `steps`, `expected_result`, `covers`, `module`.

## Automoción
Para UDS: precondición ECU en sesión correcta, request, response esperada, timeout y NRC esperado.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

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
