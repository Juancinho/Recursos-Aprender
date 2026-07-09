# Trazabilidad

Trazabilidad es la capacidad de ir de requisito a tests, código, defectos y evidencias. En automatización de testing es el mapa de responsabilidad.

## Conecta con
- [[Testing_basado_en_requisitos]]
- [[Coverage_Gaps_Duplicados_Contradicciones]]

## Relación mínima
`requirement_id -> test_case_id -> result -> evidence`.

## Por qué importa
Sin trazabilidad no sabes si un cambio rompe una obligación contractual o de seguridad.

## Formato práctico
CSV con columnas `requirement_id,test_id,relation,confidence,reviewed_by`.

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
