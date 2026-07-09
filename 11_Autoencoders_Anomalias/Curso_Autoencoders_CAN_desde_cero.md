# Curso autoencoders para anomalias CAN desde cero

## 1. Idea basica

Un autoencoder aprende a reconstruir su entrada:

```text
x -> encoder -> latent -> decoder -> x_reconstruido
```

Si entrenas solo con datos normales, deberia reconstruir bien patrones normales y reconstruir peor patrones anormales.

La anomalia se mide con error de reconstruccion:

```text
error = ||x - x_reconstruido||
```

## 2. Por que puede servir en CAN

El trafico CAN suele tener estructura:

- IDs periodicos;
- DLC estable;
- payload con patrones;
- deltas de tiempo regulares;
- ciertos IDs aparecen con frecuencia concreta.

Una anomalia puede ser:

- ID inesperado;
- frecuencia anormal;
- payload raro;
- cambio brusco;
- mensajes ausentes;
- burst de mensajes.

## 3. Features

Features basicas:

```text
timestamp
delta_time
can_id_int
dlc
b0 ... b7
```

Features mas avanzadas:

- frecuencia por ID en ventana;
- entropia del payload;
- diferencia contra payload anterior del mismo ID;
- rolling mean de delta_time;
- indicador de ID visto/no visto.

## 4. Entrenar solo con normal

Si mezclas anomalias en entrenamiento, el autoencoder puede aprender a reconstruirlas. Para deteccion no supervisada/semi-supervisada:

1. entrena con normal;
2. calcula errores en validacion normal;
3. define threshold;
4. evalua con anomalias.

## 5. Threshold percentil 99

Una regla simple:

```text
threshold = percentil_99(error_normal)
```

Eso significa: solo el 1% de normal queda por encima. Si un nuevo frame supera ese error, lo marcas como sospechoso.

Tradeoff:

- threshold bajo: mas falsos positivos;
- threshold alto: mas falsos negativos.

## 6. Limitaciones

Un autoencoder no entiende "ataque" de forma semantica. Detecta rareza estadistica respecto al entrenamiento.

Puede fallar si:

- el entrenamiento no representa bien lo normal;
- hay drift temporal;
- features pobres;
- normalizacion incorrecta;
- anomalia se parece a normal.

## 7. Ejercicio

```bash
python 13_Labs/code/can_autoencoder.py
```

Debes observar:

- dataset sintetico si no existe;
- normalizacion;
- entrenamiento;
- reconstruction error;
- threshold;
- metricas basicas.

## 8. Autocomprobacion

- [ ] Puedo dibujar encoder-latent-decoder.
- [ ] Puedo explicar reconstruction error.
- [ ] Puedo proponer 5 features CAN.
- [ ] Puedo explicar por que entrenar con normal.
- [ ] Puedo explicar falso positivo/falso negativo en anomalias.

