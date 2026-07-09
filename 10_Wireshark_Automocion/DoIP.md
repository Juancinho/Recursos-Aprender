# DoIP

DoIP transporta diagnóstico sobre IP. En Wireshark suele convivir con TCP/UDP y puertos de diagnóstico.

## Conecta con
- [[Wireshark]]
- [[UDS]]

## Idea
UDS no tiene por qué ir solo sobre CAN; puede viajar sobre IP mediante DoIP.

## Filtro
`doip` o filtros por puerto si el dissector no reconoce todo.

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
