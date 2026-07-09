# Ejercicio autoencoder CAN

## Objetivo

Generar un dataset CAN sintético, entrenar un autoencoder simple y detectar anomalías por reconstruction error.

## Comando

```bash
python 13_Labs/code/can_autoencoder.py
```

## Qué deberías observar

- Se crea `can_synthetic.csv`.
- Se entrena con muestras normales.
- Se calcula threshold percentil 99.
- Se imprimen métricas básicas.

## Entregable

- [ ] Número de anomalías detectadas.
- [ ] Threshold usado.
- [ ] Dos ejemplos de falso positivo/falso negativo si aparecen.

## Lección guiada

En autoencoders, la pregunta no es "¿entrena?", sino "¿qué considera normal y qué errores produce?".

### Preguntas

- ¿Entrené solo con normal?
- ¿Qué features uso?
- ¿Cómo normalicé?
- ¿Cómo elegí threshold?
- ¿Qué falsos positivos aparecen?

### Práctica

```bash
python 13_Labs/code/can_autoencoder.py
```

### Evidencia

- [ ] Puedo explicar reconstruction error.
- [ ] Puedo justificar percentil 99.
- [ ] Puedo distinguir anomalía estadística de fallo real.
