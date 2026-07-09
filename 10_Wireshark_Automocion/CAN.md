# CAN

CAN es un bus de comunicación muy usado en automoción. Un frame CAN contiene un arbitration ID, longitud de datos y payload.

## Campos

- timestamp: cuándo se vio.
- arbitration ID / CAN ID: identifica prioridad y mensaje.
- DLC: data length code.
- payload: hasta 8 bytes en CAN clásico.
- periodicidad: muchos mensajes aparecen cada X ms.

## Ejemplo tabular

| timestamp | can_id | dlc | payload |
|---:|---|---:|---|
| 0.010 | 0x123 | 8 | 01 02 03 04 05 06 07 08 |

## Para autoencoders

Features típicas: `can_id_int`, `dlc`, `delta_time`, `b0..b7`, frecuencia por ID, entropía y diferencias de payload. Ver [[Features_para_CAN]].

## Ampliación curso: CAN desde el punto de vista de datos

En CAN, el ID no es una dirección de origen/destino como IP. Es un identificador de mensaje y también participa en arbitraje/prioridad. IDs más bajos tienen mayor prioridad en el bus clásico.

### Periodicidad

Muchos mensajes de estado se envían cada 10 ms, 20 ms, 100 ms, etc. Una anomalía puede ser:

- mensaje esperado que desaparece;
- frecuencia demasiado alta;
- frecuencia demasiado baja;
- payload fuera de patrón;
- DLC incorrecto;
- ID desconocido.

### De frame a fila de ML

```text
timestamp, can_id_int, dlc, delta_time, b0, b1, b2, b3, b4, b5, b6, b7
```

### Limitación

Un byte no siempre es una señal completa. A veces una señal ocupa bits dentro de varios bytes, con endianess y escala definidos en DBC. Si tienes DBC, úsalo; si no, empieza por patrones estadísticos.

## Lección guiada

En Wireshark/automoción, primero lee paquetes, después modela. No entrenes un autoencoder sobre columnas que no sabes interpretar.

### Preguntas

- ¿Qué timestamp tiene?
- ¿Qué protocolo es?
- ¿Cuál es el CAN ID o endpoint?
- ¿Qué DLC/payload aparece?
- ¿Es request, response o tráfico periódico?

### Práctica

Usa filtros:

```text
can
isotp
uds
doip
tcp.port == 13400
frame contains ...
```

### Evidencia

- [ ] Puedo explicar un frame CAN.
- [ ] Puedo explicar DID y NRC.
- [ ] Puedo proponer features para anomalías.
