# Recursos vLLM LiteLLM Qwen

## Enlaces

- https://docs.vllm.ai/
- https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/
- https://docs.litellm.ai/
- https://qwen.readthedocs.io/

## Cómo usar esta nota

- [ ] Abre un enlace cuando estés haciendo un lab relacionado.
- [ ] Resume en una nota propia el comando o idea que te sirvió.
- [ ] No acumules recursos sin convertirlos en práctica.

## Lección guiada

Un recurso externo solo cuenta si lo conviertes en práctica.

- [ ] He abierto el recurso con una pregunta concreta.
- [ ] He extraído un comando, concepto o limitación.
- [ ] Lo he enlazado con una nota técnica.
- [ ] He descartado lo que no necesito ahora.

## Referencias guiadas inferencia

- vLLM docs: https://docs.vllm.ai/
  - Mira: OpenAI-compatible server, server arguments, quantization.
- LiteLLM docs: https://docs.litellm.ai/
  - Mira: proxy, model list, routing.
- Qwen docs: https://qwen.readthedocs.io/
  - Mira: modelos, serving, context length.
- PagedAttention paper: https://arxiv.org/abs/2309.06180
  - Mira: KV cache, memory fragmentation, throughput.

## Después de leer

- [ ] Escribe un `curl` a `/v1/chat/completions`.
- [ ] Dibuja OpenWebUI -> LiteLLM -> vLLM -> Qwen.
- [ ] Explica TTFT, throughput y streaming.
