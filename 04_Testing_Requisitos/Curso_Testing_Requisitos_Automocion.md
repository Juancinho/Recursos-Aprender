# Curso testing basado en requisitos de automocion

## 1. Que es un requisito

Un requisito describe una propiedad, comportamiento o restriccion que el sistema debe cumplir. En automocion puede hablar de diagnostico, red, ECU, tiempos, seguridad, luces, carroceria o comunicaciones.

Ejemplo:

```text
REQ-001: The ECU shall support UDS service 0x22 ReadDataByIdentifier.
```

Un buen requisito deberia ser:

- claro;
- verificable;
- no ambiguo;
- trazable;
- lo bastante atomico para poder testearse.

## 2. Specification vs requirement

Una especificacion puede contener muchos requisitos. El requisito es una unidad testeable. En documentos reales, la frontera no siempre esta limpia. Parte del trabajo consiste en extraer unidades verificables.

Ejemplo:

```text
Specification section 4.2:
The diagnostic module shall support ReadDataByIdentifier and shall return NRC 0x31 for unsupported DIDs.
```

Podrias separar:

- soporte de servicio `0x22`;
- comportamiento ante DID soportado;
- comportamiento ante DID no soportado;
- NRC esperado `0x31`.

## 3. Test case

Un test case es una forma concreta de verificar un requisito:

```text
TC-001:
Precondition: ECU online.
Steps:
1. Send UDS request 0x22 F190.
2. Wait response.
Expected:
Positive response 0x62 F190 with VIN bytes.
```

Un test case no es solo un nombre. Debe tener precondiciones, pasos, input y expected result.

## 4. Trazabilidad

La trazabilidad responde:

```text
que test cubre que requisito?
```

Tabla minima:

| requirement_id | test_id | relation | confidence |
|---|---|---|---|
| REQ-001 | TC-001 | covers | high |
| REQ-002 | TC-014 | partially_covers | medium |

Esto permite detectar:

- requisitos sin test;
- tests sin requisito;
- cobertura parcial;
- duplicados;
- contradicciones.

## 5. Gap, duplicado y contradiccion

**Gap**: falta cobertura o falta requisito.

```text
REQ dice que debe devolver NRC 0x31, pero no hay test negativo.
```

**Duplicado**: dos requisitos dicen casi lo mismo.

```text
REQ-010 y REQ-044 ambos exigen soporte de ReadDataByIdentifier.
```

**Contradiccion**: dos requisitos imponen comportamientos incompatibles.

```text
REQ-A: unsupported DID -> NRC 0x31
REQ-B: unsupported DID -> NRC 0x13
```

## 6. Verificacion vs validacion

Verificacion:

```text
Construimos bien lo especificado?
```

Validacion:

```text
Lo especificado sirve para la necesidad real?
```

En prácticas de IA probablemente trabajaras mas con verificacion documental y trazabilidad, pero debes conocer la diferencia.

## 7. Como ayuda IA aqui

Un sistema con retrieval puede:

- buscar requisitos similares;
- sugerir tests candidatos;
- detectar gaps;
- detectar duplicados;
- encontrar contradicciones;
- generar borradores de test cases;
- explicar por que relaciona dos items.

Pero no debe decidir sin evaluacion. Necesitas golden set.

## 8. Golden set

Un golden set es un conjunto pequeño y revisado manualmente que sirve para evaluar.

Ejemplo:

```csv
query_requirement, relevant_requirement, relation
REQ-001,REQ-014,duplicate
REQ-002,TC-003,covers
REQ-008,REQ-021,contradiction
```

Con esto mides si BM25, embeddings o hybrid search encuentran lo que deben.

## 9. Dataset recomendado

Columnas para `requirements.csv`:

```csv
id,module,domain,text,priority,version
REQ-001,diagnostics,UDS,The ECU shall support UDS service 0x22 ReadDataByIdentifier.,high,v1
REQ-002,diagnostics,UDS,The ECU shall return NRC 0x31 when the DID is unsupported.,high,v1
REQ-003,network,DoIP,The gateway shall accept DoIP diagnostic sessions over TCP port 13400.,medium,v1
```

Columnas para `tests.csv`:

```csv
id,module,requirement_id,title,steps,expected
TC-001,diagnostics,REQ-001,Read DID F190,Send 22 F190,Receive 62 F190
```

## 10. Autocomprobacion

- [ ] Puedo convertir un parrafo largo en requisitos atomicos.
- [ ] Puedo escribir un test case verificable.
- [ ] Puedo detectar un gap.
- [ ] Puedo explicar por que un golden set es necesario.
- [ ] Puedo justificar por que retrieval no sustituye la revision humana.

