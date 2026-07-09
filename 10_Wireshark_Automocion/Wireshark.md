# Wireshark

Wireshark permite capturar y analizar paquetes. En automoción puede aparecer para Ethernet/DoIP, trazas pcap/pcapng y, con soporte adecuado, CAN/UDS/ISO-TP.

## Conceptos

- pcap/pcapng: archivos de captura.
- display filter: filtro de visualización, no modifica la captura.
- frame: paquete capturado.
- timestamp: momento de captura.
- payload: datos útiles.

## Filtros básicos

```text
ip.addr == 192.168.0.10
tcp
udp
tcp.port == 13400
frame contains "UDS"
can
isotp
uds
doip
```

## Cómo no perderse

1. Filtra por protocolo.
2. Ordena por tiempo.
3. Identifica request/response.
4. Mira campos, no solo bytes.
5. Exporta subconjuntos pequeños para estudiar.

## Ampliación curso: leer una captura como una historia temporal

Una captura no es una tabla aleatoria. Es una historia ordenada por tiempo. Para entenderla:

1. Identifica el intervalo.
2. Filtra protocolos.
3. Busca patrones periódicos.
4. Busca pares request/response.
5. Marca errores o timeouts.
6. Relaciona bytes con señales o servicios.

### Capas de lectura

| Capa | Pregunta |
|---|---|
| Tiempo | ¿cuándo ocurre y con qué periodicidad? |
| Transporte | ¿CAN, TCP, UDP, DoIP? |
| Protocolo | ¿UDS, ISO-TP, diagnóstico? |
| Payload | ¿qué bytes cambian? |
| Semántica | ¿qué significa para ECU/test? |

### Para datasets de anomalías

No metas la captura cruda al modelo sin pensar. Primero decide features:

- delta entre mensajes;
- ID;
- DLC;
- bytes;
- frecuencia por ID;
- cambios de payload;
- secuencias request/response.

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
