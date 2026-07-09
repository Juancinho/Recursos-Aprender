# LiteLLM

LiteLLM actúa como gateway/proxy para modelos. Unifica APIs, claves, nombres de modelo, routing y observabilidad.

## Conecta con
- [[Motor_de_inferencia]]
- [[OpenAI_Compatible_API]]

## Uso
OpenWebUI llama a LiteLLM; LiteLLM decide si manda a vLLM, OpenAI, Azure u otro backend.

## Ventaja
Cambiar proveedor sin cambiar clientes.

## Pregunta clave
¿LiteLLM está solo como proxy o también aplica políticas, logs y budgets?

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Lección guiada

En inferencia, distingue modelo, servidor, gateway y cliente. Muchos errores parecen "del modelo" pero son de endpoint, streaming, memoria o configuración.

### Preguntas

- ¿Quién expone `/v1/chat/completions`?
- ¿Qué modelo real hay detrás del nombre?
- ¿Hay LiteLLM entre OpenWebUI y vLLM?
- ¿La lentitud está en prefill o decode?
- ¿Qué consume KV cache?

### Práctica

```bash
curl http://localhost:8000/v1/models
curl http://localhost:8000/v1/chat/completions
```

### Evidencia

- [ ] Puedo explicar KV cache.
- [ ] Puedo explicar batching y streaming.
- [ ] Sé qué preguntar sobre Qwen local.
