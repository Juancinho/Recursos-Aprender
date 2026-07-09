# Ruta de visionado y lectura por semana

Esta ruta acompaña a [[Plan_10_Semanas]]. No está pensada para verlo todo de golpe. Cada semana tiene recursos mínimos, recursos opcionales y una práctica obligatoria.

## Semana 1: Docker

**Mínimo**

- Docker Get Started: https://docs.docker.com/get-started/
- Docker Compose docs: https://docs.docker.com/compose/
- Volumes: https://docs.docker.com/engine/storage/volumes/
- Windows install: https://docs.docker.com/desktop/setup/install/windows-install/

**Qué mirar**

- containers vs images;
- publishing ports;
- persisting data;
- compose services.

**Práctica**

- [ ] [[Lab_01_Docker_Nginx]]
- [ ] [[Lab_02_Docker_Compose]]

## Semana 2: Git, diff, patch y repos

**Mínimo**

- Pro Git book: https://git-scm.com/book/en/v2
- `git diff`: https://git-scm.com/docs/git-diff
- `git apply`: https://git-scm.com/docs/git-apply

**Qué mirar**

- historial;
- diff;
- patches;
- búsqueda en repo;
- ramas solo si las necesitas.

**Práctica**

- [ ] [[Lab_03_Patch_al_arrancar]]
- [ ] crear `MAPA_REPO.md`

## Semana 3: requirements testing

**Mínimo**

- ISTQB glossary: https://glossary.istqb.org/
- CTFL: https://www.istqb.org/certifications/certified-tester-foundation-level

**Qué mirar**

- requirement;
- test case;
- verification/validation;
- regression testing;
- traceability.

**Práctica**

- [ ] [[Lab_04_Dataset_Requisitos]]

## Semana 4: embeddings y thresholds

**Mínimo**

- Hugging Face Course: https://huggingface.co/learn/llm-course/chapter1/1
- Sentence Transformers docs: https://www.sbert.net/
- scikit-learn cosine similarity: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

**Qué mirar**

- embeddings;
- vector similarity;
- cosine similarity;
- false positives/false negatives.

**Práctica**

- [ ] [[Lab_05_Embeddings_Thresholds]]

## Semana 5: BM25 e hybrid search

**Mínimo**

- Introduction to Information Retrieval: https://nlp.stanford.edu/IR-book/
- rank-bm25: https://pypi.org/project/rank-bm25/
- Qdrant hybrid queries: https://qdrant.tech/documentation/search/hybrid-queries/

**Qué mirar**

- lexical retrieval;
- term frequency;
- inverse document frequency;
- RRF;
- dense+sparse.

**Práctica**

- [ ] [[Lab_06_BM25_Hybrid]]

## Semana 6: Qdrant

**Mínimo**

- Qdrant documentation: https://qdrant.tech/documentation/
- Collections: https://qdrant.tech/documentation/concepts/collections/
- Points: https://qdrant.tech/documentation/concepts/points/
- Search: https://qdrant.tech/documentation/search/
- Filtering: https://qdrant.tech/documentation/concepts/filtering/

**Qué mirar**

- collections;
- points;
- payload;
- filters;
- distance metrics.

**Práctica**

- [ ] [[Lab_07_Qdrant]]

## Semana 7: OpenWebUI parcheado

**Mínimo**

- OpenWebUI docs: https://docs.openwebui.com/
- RAG in OpenWebUI: https://docs.openwebui.com/features/chat-conversations/rag/
- GitHub repo: https://github.com/open-webui/open-webui

**Qué mirar**

- Docker quick start;
- OpenAI-compatible providers;
- RAG;
- external vector databases;
- environment variables.

**Práctica**

- [ ] [[Lab_08_OpenWebUI_Arquitectura]]

## Semana 8: vLLM, LiteLLM y Qwen

**Mínimo**

- vLLM docs: https://docs.vllm.ai/
- vLLM OpenAI-compatible server: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/
- LiteLLM docs: https://docs.litellm.ai/
- Qwen docs: https://qwen.readthedocs.io/
- PagedAttention paper: https://arxiv.org/abs/2309.06180

**Qué mirar**

- OpenAI-compatible API;
- streaming;
- batching;
- KV cache;
- quantization;
- context length.

**Práctica**

- [ ] [[Lab_09_vLLM_LiteLLM]]

## Semana 9: Qodo, code embeddings, LangGraph y MCP

**Mínimo**

- Qodo docs: https://docs.qodo.ai/
- Qodo code embeddings: https://www.qodo.ai/products/code-embedding/
- LangGraph Graph API: https://docs.langchain.com/oss/python/langgraph/graph-api
- MCP intro: https://modelcontextprotocol.io/docs/getting-started/intro

**Qué mirar**

- code embeddings;
- natural language to code;
- graph state;
- nodes/edges;
- tool schemas.

**Práctica**

- [ ] [[Lab_10_Code_Embeddings]]

## Semana 10: Wireshark, CAN, UDS, DoIP y autoencoders

**Mínimo**

- Wireshark User Guide: https://www.wireshark.org/docs/wsug_html/
- Wireshark display filters: https://www.wireshark.org/docs/man-pages/wireshark-filter.html
- Scapy automotive: https://scapy.readthedocs.io/en/latest/layers/automotive.html
- PyTorch tutorials: https://pytorch.org/tutorials/

**Qué mirar**

- display filters;
- packet list/details/bytes;
- CAN/UDS layers;
- tensors;
- training loop.

**Práctica**

- [ ] [[Lab_12_Wireshark_CAN]]
- [ ] [[Lab_13_Autoencoder_CAN]]

## Atención entre requisitos: transversal

**Mínimo**

- Illustrated Transformer: https://jalammar.github.io/illustrated-transformer/
- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- PyTorch scaled dot-product attention: https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
- Hugging Face Transformers docs: https://huggingface.co/docs/transformers/index

**Práctica**

- [ ] [[Lab_11_Atencion_Requisitos]]
