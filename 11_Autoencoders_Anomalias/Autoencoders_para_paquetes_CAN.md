# Autoencoders para paquetes CAN

CAN es adecuado para detección de anomalías porque muchos mensajes son periódicos y tienen patrones de payload.

## Conecta con
- [[Autoencoders]]
- [[Features_para_CAN]]
- [[CAN]]

## Features
`timestamp`, `delta_time`, `can_id`, `dlc`, `byte_0..byte_7`, frecuencia por ID, entropía.

## Entrenamiento
Usa solo tráfico normal. Evalúa en normal + anomalías sintéticas o etiquetadas.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

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
