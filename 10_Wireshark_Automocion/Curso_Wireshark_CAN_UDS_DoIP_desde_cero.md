# Curso Wireshark, CAN, UDS y DoIP desde cero

## 1. Que estas mirando en Wireshark

Wireshark muestra paquetes o frames capturados. No es solo una tabla: cada fila es una observacion de comunicacion en el tiempo.

En automocion puedes ver:

- Ethernet/IP/TCP/UDP;
- DoIP;
- CAN;
- ISO-TP;
- UDS.

## 2. Anatomia de una captura

Campos comunes:

- timestamp;
- numero de frame;
- origen;
- destino;
- protocolo;
- longitud;
- informacion decodificada.

La clave es no perderte: empieza por filtrar.

## 3. Filtros utiles

```text
ip.addr == 192.168.0.10
tcp
udp
tcp.port == 13400
can
isotp
uds
doip
frame contains "22"
```

> [!warning]
> Un display filter no modifica la captura. Solo cambia lo que ves.

## 4. CAN frame

Un frame CAN suele tener:

- arbitration ID;
- DLC;
- payload;
- timestamp.

Ejemplo conceptual:

```text
time=1.234 can_id=0x7E0 dlc=8 data=03 22 F1 90 00 00 00 00
```

Interpretacion:

- `0x7E0`: posible request a ECU;
- `03`: longitud ISO-TP single frame;
- `22`: UDS ReadDataByIdentifier;
- `F1 90`: DID.

## 5. UDS

UDS define servicios diagnosticos.

Ejemplos:

| SID | Nombre |
|---|---|
| 0x10 | DiagnosticSessionControl |
| 0x11 | ECUReset |
| 0x22 | ReadDataByIdentifier |
| 0x2E | WriteDataByIdentifier |
| 0x19 | ReadDTCInformation |

Respuesta positiva:

```text
request SID + 0x40
```

Para `0x22`, respuesta positiva `0x62`.

Respuesta negativa:

```text
0x7F <SID original> <NRC>
```

Ejemplo:

```text
7F 22 31
```

Significa respuesta negativa al servicio `0x22` con NRC `0x31`.

## 6. ISO-TP

CAN tiene payload pequeno. ISO-TP permite transportar mensajes mas largos fragmentandolos.

Tipos:

- Single Frame;
- First Frame;
- Consecutive Frame;
- Flow Control.

Si no entiendes ISO-TP, puedes confundir fragmentos con mensajes completos.

## 7. DoIP

DoIP transporta diagnostico sobre IP. Puede aparecer sobre TCP, por ejemplo puerto 13400. La idea de UDS sigue, pero el transporte cambia.

```text
UDS sobre CAN -> CAN + ISO-TP
UDS sobre Ethernet -> DoIP + TCP/IP
```

## 8. Como leer sin perderte

1. Identifica protocolo.
2. Filtra por conversacion.
3. Mira timestamp y periodicidad.
4. Separa request/response.
5. Decodifica SID, DID, NRC.
6. Anota payload bruto.
7. Relaciona con requisito/test.

## 9. Autocomprobacion

- [ ] Puedo explicar arbitration ID, DLC y payload.
- [ ] Puedo distinguir CAN de UDS.
- [ ] Puedo reconocer `0x22`, `0x62` y `0x7F`.
- [ ] Puedo explicar que es NRC.
- [ ] Puedo explicar diferencia entre UDS sobre CAN y UDS sobre DoIP.

