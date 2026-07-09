# Ejercicios Wireshark CAN

## Objetivo

Practicar lectura de campos antes de entrenar modelos.

## Tareas

- [ ] Abrir una captura pcap/pcapng si la empresa te da una.
- [ ] Filtrar `can` o `doip`.
- [ ] Identificar 5 mensajes periódicos.
- [ ] Anotar CAN ID, DLC, payload y delta_time.
- [ ] Buscar una request UDS y su response.
- [ ] Anotar si hay NRC.

## Entregable

Una tabla con 10 frames y una explicación de qué crees que ocurre.

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
