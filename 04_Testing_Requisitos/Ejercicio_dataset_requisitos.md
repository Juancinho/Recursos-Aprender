# Ejercicio dataset requisitos

## Objetivo

Crear `requirements.csv` y `tests.csv` con requisitos de automoción: diagnostics, body, lighting, UDS, CAN, DoIP.

## Pasos

1. Ejecuta:

```bash
python 13_Labs/code/requirements_dataset.py
python 13_Labs/code/coverage_checker.py
```

2. Abre los CSV generados en `13_Labs/outputs/`.
3. Añade manualmente 3 relaciones:
   - una correcta
   - una dudosa
   - una incorrecta

## Qué estás haciendo

Estás convirtiendo texto en datos evaluables. Sin esto, un sistema de IA solo puede dar impresiones; con esto puedes medir coverage y errores.

## Entregable

- [ ] `requirements.csv`
- [ ] `tests.csv`
- [ ] tabla de coverage
- [ ] 3 dudas escritas

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
