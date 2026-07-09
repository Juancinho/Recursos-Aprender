# Biblioteca comentada

Esta biblioteca no es una lista para acumular. Cada recurso tiene una razón de uso y una acción asociada.

## Infraestructura

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://docs.docker.com/get-started/ | oficial | fundamentos de Docker | repetir [[Lab_01_Docker_Nginx]] |
| https://docs.docker.com/compose/ | oficial | multi-servicio | anotar un Compose real |
| https://docs.docker.com/engine/storage/volumes/ | oficial | persistencia | explicar volumen de Qdrant |

## Git y patches

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://git-scm.com/book/en/v2 | libro | modelo mental Git | leer capítulos 2 y 7 |
| https://git-scm.com/docs/git-diff | referencia | entender diffs | leer opciones básicas |
| https://git-scm.com/docs/git-apply | referencia | aplicar patches | practicar `--check` |

## Testing

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://glossary.istqb.org/ | glosario | vocabulario preciso | buscar 10 términos |
| https://www.istqb.org/certifications/certified-tester-foundation-level | certificación | temario testing base | mapear términos a notas |

## Retrieval y vector databases

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://nlp.stanford.edu/IR-book/ | libro | IR, BM25, evaluación | leer ranking/evaluation |
| https://qdrant.tech/documentation/ | oficial | Qdrant general | crear colección |
| https://qdrant.tech/documentation/search/hybrid-queries/ | oficial | hybrid search | comparar con [[Lab_06_BM25_Hybrid]] |
| https://www.sbert.net/ | docs | sentence embeddings | cambiar modelo del lab |

## OpenWebUI

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://docs.openwebui.com/ | oficial | arquitectura y arranque | identificar quick start |
| https://docs.openwebui.com/features/chat-conversations/rag/ | oficial | RAG y vector DB externa | revisar campos de mapping |
| https://github.com/open-webui/open-webui | repo | código fuente | practicar [[Como_leer_un_repo_grande_sin_IA]] |

## Inferencia

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://docs.vllm.ai/ | oficial | serving | localizar OpenAI-compatible server |
| https://docs.litellm.ai/ | oficial | gateway | dibujar routing |
| https://qwen.readthedocs.io/ | oficial | modelos Qwen | anotar variantes/contexto |
| https://arxiv.org/abs/2309.06180 | paper | PagedAttention/KV cache | resumir problema de memoria |

## Code embeddings y agentes

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://docs.qodo.ai/ | oficial | plataforma Qodo | distinguir producto vs embeddings |
| https://www.qodo.ai/products/code-embedding/ | producto/modelo | Qodo-Embed | anotar NL->code/code->code |
| https://docs.langchain.com/oss/python/langgraph/graph-api | oficial | nodos/edges/state | dibujar workflow |
| https://modelcontextprotocol.io/docs/getting-started/intro | oficial | MCP | diseñar una tool segura |

## Automoción

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://www.wireshark.org/docs/wsug_html/ | manual | interfaz y paquetes | abrir captura y filtrar |
| https://www.wireshark.org/docs/man-pages/wireshark-filter.html | referencia | display filters | crear chuleta |
| https://scapy.readthedocs.io/en/latest/layers/automotive.html | docs | capas automotive | mirar CAN/UDS en Python |

## Transformers y atención

| Recurso | Tipo | Úsalo para | Acción |
|---|---|---|---|
| https://jalammar.github.io/illustrated-transformer/ | visual | intuición Transformer | dibujar Q/K/V |
| https://arxiv.org/abs/1706.03762 | paper | atención original | leer sección attention |
| https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html | API | implementación PyTorch | comparar con script desde cero |
| https://huggingface.co/docs/transformers/index | docs | modelos y attentions | ejecutar lab transformer |
