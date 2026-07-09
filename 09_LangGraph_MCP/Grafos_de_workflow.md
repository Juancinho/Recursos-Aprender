# Grafos de workflow

Un grafo hace explícito qué pasos existen y qué datos pasan de uno a otro. Es más auditable que un prompt gigante.

## Conecta con
- [[LangGraph]]
- [[Ejemplo_workflow_requirements_testing]]

## Nodos
normalizar requisito, embeddings, búsqueda Qdrant, scoring, LLM, validación, revisión humana.

## Estado
`input_requirement`, `candidates`, `scores`, `llm_json`, `validated_result`.

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
