# Coverage, Gaps, Duplicados y Contradicciones

Estos son patrones que un sistema de retrieval/LLM puede ayudar a encontrar, pero siempre con revisión humana.

## Conecta con
- [[Testing_basado_en_requisitos]]
- [[Evaluacion_Retrieval]]

## Coverage
Un requisito está cubierto si hay al menos un test relevante y ejecutable.

## Gap
No hay test o el test no comprueba lo esencial.

## Duplicado
Dos requisitos tienen el mismo comportamiento con distinta redacción.

## Contradicción
Ejemplo: un requisito exige responder NRC 0x31 y otro exige positive response para el mismo caso.

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
