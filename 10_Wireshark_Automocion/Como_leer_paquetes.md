# Cómo leer paquetes

Leer paquetes es separar capas: tiempo, transporte, protocolo, payload y relación request/response.

## Conecta con
- [[Wireshark]]
- [[CAN]]
- [[UDS]]
- [[DoIP]]

## Método
Empieza por timestamp y protocolo. Luego identifica origen/destino o CAN ID. Después interpreta payload.

## Preguntas
¿Es periódico? ¿Es respuesta a algo? ¿Hay error/NRC? ¿Cambió el payload cuando cambió el estado?

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
