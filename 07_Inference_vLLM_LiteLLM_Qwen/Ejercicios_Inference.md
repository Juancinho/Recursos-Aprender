# Ejercicios Inference

## Ejercicio 1: dibujar arquitectura

Dibuja OpenWebUI -> LiteLLM -> vLLM -> Qwen y anota puertos, variables y logs.

## Ejercicio 2: curl

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer dummy" \
  -d '{"model":"qwen-local","messages":[{"role":"user","content":"ping"}]}'
```

## Ejercicio 3: variables típicas

- `OPENAI_API_BASE_URL`
- `OPENAI_API_KEY`
- `LITELLM_MASTER_KEY`
- `MODEL_NAME`
- `VLLM_HOST`
- `VLLM_PORT`

## Preguntas para empresa

- [ ] ¿Qué modelo Qwen?
- [ ] ¿Qué contexto?
- [ ] ¿Qué cuantización?
- [ ] ¿Qué GPU?
- [ ] ¿Qué puerto?
- [ ] ¿Hay streaming?
- [ ] ¿Hay LiteLLM en medio?
- [ ] ¿Dónde están logs de vLLM?

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
