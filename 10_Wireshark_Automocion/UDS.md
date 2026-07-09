# UDS

UDS (Unified Diagnostic Services) es un protocolo de diagnóstico usado para hablar con ECUs.

## Conceptos

- Service ID: identifica el servicio, por ejemplo `0x22` ReadDataByIdentifier.
- DID: Data Identifier.
- NRC: Negative Response Code, por ejemplo `0x31` request out of range.
- ISO-TP: transporte para mensajes que no caben en un frame CAN.

## Ejemplo

REQ_A: "The ECU shall support UDS service 0x22 ReadDataByIdentifier."

REQ_B: "The diagnostic module shall return NRC 0x31 when the DID is unsupported."

Estos requisitos están relacionados pero no son equivalentes. Retrieval y atención token-a-token pueden ayudar a inspeccionar la relación.

## Ampliación curso: UDS como diálogo

UDS se entiende mejor como request/response.

### Positive response

Para muchos servicios, la respuesta positiva es `service_id + 0x40`. Por ejemplo:

- request `0x22`
- positive response `0x62`

### Negative response

Una respuesta negativa suele incluir:

- `0x7F`;
- service ID original;
- NRC.

Ejemplo conceptual:

```text
Request:  22 F1 90
Response: 7F 22 31
```

Interpretación: petición ReadDataByIdentifier, rechazada con NRC `0x31`.

### Para requisitos/testing

Un requisito UDS casi siempre debe especificar:

- servicio;
- sesión/precondición;
- DID o subfunction;
- respuesta positiva o NRC;
- timeout;
- transporte CAN/DoIP si aplica.

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
