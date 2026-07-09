# vLLM

vLLM es un motor de inferencia para servir LLMs con alto throughput, API OpenAI-compatible, batching continuo y gestión eficiente de KV cache.

## Conecta con
- [[Motor_de_inferencia]]
- [[KV_Cache_Batching_Streaming]]
- [[Qwen_Local]]

## Qué hace
Carga el modelo, tokeniza, gestiona peticiones concurrentes, reutiliza KV cache y devuelve tokens.

## OpenAI-compatible
Permite usar clientes que esperan `/v1/chat/completions`.

## Comando típico
`python -m vllm.entrypoints.openai.api_server --model Qwen/... --host 0.0.0.0 --port 8000`.

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
