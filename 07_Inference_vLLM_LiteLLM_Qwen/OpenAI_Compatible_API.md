# OpenAI Compatible API

Una API OpenAI-compatible imita endpoints y formatos de OpenAI para que clientes existentes funcionen con modelos locales.

## Endpoint principal

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer dummy" \
  -d '{
    "model": "qwen-local",
    "messages": [
      {"role": "user", "content": "Resume qué es UDS en una frase."}
    ],
    "stream": false
  }'
```

## Streaming

Con `"stream": true`, el servidor devuelve eventos parciales. OpenWebUI lo usa para mostrar tokens según llegan.

## Qué verificar

- URL base.
- nombre del modelo.
- clave requerida.
- endpoint `/models`.
- soporte streaming.
- formato de errores.

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
