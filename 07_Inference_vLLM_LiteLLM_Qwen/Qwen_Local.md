# Qwen Local

Qwen local es el modelo ejecutado en infraestructura propia. Debes distinguir variante, tamaño, cuantización y contexto.

## Conecta con
- [[vLLM]]
- [[LiteLLM]]
- [[Motor_de_inferencia]]

## Preguntas
¿Qué modelo Qwen exacto? ¿Cuántos parámetros? ¿Context length? ¿Cuantización? ¿GPU? ¿vLLM args?

## Riesgo
Un Qwen pequeño puede ser rápido pero fallar razonamiento; uno grande puede no caber en GPU sin cuantización.

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
