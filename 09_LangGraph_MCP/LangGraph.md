# LangGraph

LangGraph permite modelar workflows de LLM como grafos con nodos, edges y estado.

## Conecta con
- [[Grafos_de_workflow]]
- [[Herramientas_para_LLM]]
- [[MCP]]

## Conceptos
Nodo = paso. Edge = transición. Estado = datos compartidos. Tool = acción externa.

## Uso
Un flujo de testing puede recuperar requisitos, pedir análisis a LLM, validar JSON y guardar resultados.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Ampliación curso: cuándo un grafo es mejor que una cadena

Un flujo lineal sirve para tareas simples. Un grafo es útil cuando hay decisiones, reintentos, validación, revisión humana o caminos alternativos.

### Ejemplo de estado

```python
state = {
    "requirement": "...",
    "normalized_requirement": "...",
    "candidates": [],
    "scores": {},
    "llm_result": None,
    "validation_errors": [],
    "needs_human_review": False,
}
```

### Buen diseño de nodos

Cada nodo debe hacer una cosa:

- normalizar texto;
- buscar en Qdrant;
- calcular BM25;
- fusionar rankings;
- llamar al LLM;
- validar JSON;
- guardar resultado.

### Errores comunes

- Nodo gigante que hace todo.
- Estado implícito en variables globales.
- Herramientas sin schema claro.
- LLM devolviendo texto libre donde se necesita JSON.
- No tener rama de revisión humana.

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
