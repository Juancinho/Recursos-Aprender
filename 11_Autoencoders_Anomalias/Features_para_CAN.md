# Features para CAN

## Features básicas

- `timestamp`
- `delta_time`
- `can_id_int`
- `dlc`
- `byte_0` ... `byte_7`
- frecuencia por ID
- entropía
- diferencias de payload

## Decisiones

- CAN ID como entero puede inducir orden artificial.
- One-hot por ID puede ser útil si hay pocos IDs.
- `delta_time` captura periodicidad.
- Bytes normalizados a `[0,1]` facilitan entrenamiento.

## Checklist

- [ ] Relleno bytes ausentes con 0.
- [ ] Normalizo features.
- [ ] Separo normal/anómalo.
- [ ] Guardo scaler para inferencia.

## Ampliación curso: ingeniería de features CAN

### Features por frame

Estas describen un mensaje individual:

- `can_id_int`
- `dlc`
- `delta_time`
- `b0..b7`

### Features por ventana

Estas describen comportamiento agregado:

- número de frames por ID en 1 segundo;
- media/desviación de delta_time por ID;
- entropía de payload por ID;
- número de IDs desconocidos;
- ratio de NRC en tráfico diagnóstico.

### Cuándo usar ventanas

Si la anomalía es "demasiados mensajes" o "desaparece un ID", un frame aislado no basta. Necesitas ventana temporal.

### Normalización

- Bytes: dividir por 255 o estandarizar.
- `can_id_int`: cuidado, como número induce distancia artificial.
- `delta_time`: puede tener colas largas; considera clipping/log.

### Ejercicio

- [ ] Genera features por frame.
- [ ] Añade conteo por ID en ventana.
- [ ] Entrena autoencoder con y sin ventana.
- [ ] Compara falsos positivos.

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
