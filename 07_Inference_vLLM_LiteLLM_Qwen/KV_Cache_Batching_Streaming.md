# KV Cache, Batching y Streaming

## KV cache

En un Transformer autoregresivo, cada token nuevo atiende a tokens previos. La KV cache guarda claves y valores ya calculados para no recomputar todo el contexto en cada paso.

## Batching

Batching agrupa peticiones para usar mejor GPU. En serving real, las peticiones llegan en momentos distintos; motores como [[vLLM]] hacen batching continuo.

## Streaming

Streaming devuelve tokens parciales. Mejora percepción de latencia aunque la generación total tarde lo mismo o más.

## Tradeoffs

- Más contexto consume más KV cache.
- Más usuarios concurrentes consume más memoria.
- Cuantización reduce memoria pero puede afectar calidad.
- Batching mejora throughput pero puede afectar latencia individual.

> [!idea]
> Cuando un usuario dice "va lento", pregunta: ¿latencia inicial, tokens/s, cola, GPU saturada o contexto demasiado largo?

## Ampliación curso: ejemplo numérico de KV cache

Si un prompt tiene 4.000 tokens y generas 200 tokens, sin cache tendrías que reprocesar el histórico muchas veces. Con KV cache guardas representaciones de tokens previos y en cada paso solo calculas lo nuevo contra lo guardado.

### Por qué consume memoria

Para cada layer y head se guardan claves y valores. A mayor:

- número de layers,
- hidden size,
- context length,
- batch/concurrencia,

mayor memoria de KV cache.

### Batching continuo

En servidores reales, las peticiones no llegan alineadas. Continuous batching permite meter nuevas peticiones mientras otras están generando. Eso mejora uso de GPU.

### Streaming y proxies

Aunque vLLM emita streaming, un proxy intermedio puede bufferizar y romper la experiencia. Si OpenWebUI no muestra tokens parciales, revisa:

- vLLM con `stream=true`;
- LiteLLM;
- reverse proxy;
- navegador/UI.

### Preguntas de entrevista interna

- [ ] ¿Cuál es el límite de contexto real configurado?
- [ ] ¿Hay límite de concurrencia?
- [ ] ¿Se usa cuantización?
- [ ] ¿Qué métrica miráis: TTFT, tokens/s, requests/min?
- [ ] ¿Dónde se ven OOM o timeouts?

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
