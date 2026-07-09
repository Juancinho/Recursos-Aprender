# Thresholds en anomalías

El threshold convierte error continuo en decisión. Percentil 99 es un punto de partida, no una verdad.

## Conecta con
- [[Autoencoders]]
- [[Thresholds_Falsos_Positivos_Falsos_Negativos]]

## Percentil
Si threshold = p99 del error normal, aceptas que alrededor de 1% normal caiga por encima.

## Ajuste
Sube threshold para menos falsos positivos; bájalo para más sensibilidad.

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
