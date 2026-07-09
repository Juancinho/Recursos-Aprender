# Cómo usar esta bóveda

Esta bóveda está ordenada como una ruta de incorporación técnica. La secuencia importa: primero contenedores, luego patches y repos, después requisitos/testing, retrieval, OpenWebUI, motores de inferencia y finalmente automoción/anomalías.

## Regla de avance

No pases de módulo solo por haber leído. Pasa cuando puedas:

- [ ] Explicarlo con tus palabras.
- [ ] Ejecutar un comando o script.
- [ ] Reconocer dónde aparecería en el proyecto de empresa.
- [ ] Formular una pregunta técnica mejor que "no lo entiendo".

## Cómo estudiar una nota

1. Lee el resumen.
2. Mira los enlaces internos de Obsidian y abre solo los necesarios.
3. Ejecuta el lab asociado si existe.
4. Marca los checkboxes.
5. Escribe una entrada diaria en [[Diario_Estudio_Template]].

> [!warning]
> No uses Obsidian como cementerio de enlaces. Si un recurso no te ayuda a ejecutar algo, conviértelo en una nota práctica o déjalo para después.

## Ruta mínima diaria

- 20 minutos de teoría.
- 40 minutos de práctica.
- 10 minutos de diario técnico.
- 10 minutos de recapitulación: "qué sé hacer ahora que ayer no sabía".

## Ampliación curso: cómo convertir estas notas en aprendizaje real

Esta bóveda está escrita para trabajar en ciclos. Cada ciclo tiene cuatro fases:

1. **Modelo mental**: antes de memorizar comandos, entiende qué problema resuelve la herramienta.
2. **Caso mínimo**: ejecuta un ejemplo pequeño que funcione.
3. **Diagnóstico**: rompe algo a propósito y aprende a leer el error.
4. **Transferencia**: conecta lo aprendido con Technica: OpenWebUI, Qdrant, patches, requisitos, inferencia o automoción.

### Rutina por nota

Para cada nota técnica haz esto:

- [ ] Subraya mentalmente los sustantivos técnicos: contenedor, point, payload, KV cache, DID.
- [ ] Escribe una definición de una frase sin mirar.
- [ ] Ejecuta el comando o script asociado.
- [ ] Añade un ejemplo propio de la empresa o inventado.
- [ ] Escribe una pregunta que empiece por "¿dónde se configura...?", "¿qué log muestra...?" o "¿cómo se valida...?".

### Cómo saber si estás estudiando bien

Estudiar bien no es leer más páginas. Es reducir incertidumbre operativa. Por ejemplo:

- Antes: "Docker me suena, pero no sé qué mirar si OpenWebUI no arranca".
- Después: "Primero miro `docker compose ps`, luego `docker compose logs -f openwebui`, después entrypoint, variables y volúmenes".

### Señal de alarma

> [!warning]
> Si una nota te parece clara pero no puedes ejecutar nada ni explicar un fallo típico, todavía no la has aprendido.

## Lección guiada

Usa esta nota como punto de navegación. Antes de avanzar, identifica qué módulo estás estudiando, qué práctica vas a ejecutar y qué evidencia dejarás en el diario.

- [ ] He elegido una ruta concreta para hoy.
- [ ] Sé qué archivo abrir después.
- [ ] Sé qué comando, script o checklist usaré.
- [ ] He escrito una salida esperada antes de ejecutar nada.
