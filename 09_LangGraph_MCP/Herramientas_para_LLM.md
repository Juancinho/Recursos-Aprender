# Herramientas para LLM

Una herramienta convierte una intención del LLM en una acción controlada: buscar, leer, calcular, guardar.

## Conecta con
- [[MCP]]
- [[LangGraph]]

## Buenas herramientas
Entrada JSON clara, salida estructurada, errores explícitos, permisos mínimos.

## Malas herramientas
Ejecutar comandos arbitrarios o devolver blobs enormes sin estructura.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Lección guiada

En workflows, piensa en pasos verificables. Un grafo bueno hace visible qué datos entran, qué herramienta se llama y qué validación ocurre.

### Preguntas

- ¿Cuál es el estado compartido?
- ¿Qué hace cada nodo?
- ¿Qué herramienta externa se llama?
- ¿Dónde se valida JSON?
- ¿Cuándo entra revisión humana?

### Evidencia

- [ ] Puedo dibujar el workflow.
- [ ] Puedo separar nodo, edge, estado y tool.
- [ ] Puedo detectar una herramienta demasiado amplia.
