# Filtros Wireshark

Los display filters reducen ruido visual. Aprende filtros de IP/TCP/UDP y automoción.

## Conecta con
- [[Wireshark]]
- [[DoIP]]
- [[UDS]]
- [[CAN]]

## Filtros
```text
ip.addr == ...
tcp
udp
tcp.port == ...
can
isotp
uds
doip
frame contains ...
```

## Consejo
Empieza amplio y estrecha. Si filtras demasiado pronto, puedes ocultar el contexto.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

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
