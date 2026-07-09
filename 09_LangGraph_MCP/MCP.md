# MCP

Model Context Protocol define una forma estándar de exponer herramientas y recursos a clientes LLM.

## Conecta con
- [[Herramientas_para_LLM]]
- [[LangGraph]]

## Client/server
El cliente LLM pide herramientas; el servidor MCP expone operaciones concretas.

## Ejemplo
Herramienta para buscar en Qdrant, leer tests o consultar resultados.

## Riesgo
Herramientas demasiado amplias son difíciles de auditar.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Ampliación curso: MCP como frontera de herramientas

MCP permite exponer capacidades a modelos de forma estructurada. Lo importante es diseñar herramientas pequeñas y auditables.

### Ejemplo de herramienta buena

`search_requirements(query: str, module: str | None, limit: int) -> list[RequirementCandidate]`

Ventajas:

- entrada clara;
- salida validable;
- permisos limitados;
- fácil de loggear.

### Ejemplo de herramienta mala

`run_shell(command: str) -> str`

Es demasiado amplia, difícil de auditar y peligrosa.

### MCP en requirements testing

Herramientas razonables:

- buscar requisitos;
- buscar tests;
- calcular coverage;
- guardar propuesta;
- marcar revisión humana;
- leer evidencia de ejecución.

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
