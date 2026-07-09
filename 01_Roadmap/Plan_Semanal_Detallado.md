# Plan Semanal Detallado

| Día | Tiempo | Teoría | Práctica | Archivos que debo leer | Scripts que debo ejecutar | Entregable | Autocomprobación |
|---|---:|---|---|---|---|---|---|
| 1 | 90 min | Docker básico | hello-world, nginx, logs, exec | [[Docker]], [[Imagen_vs_Contenedor]], [[Comandos_Docker]] | ninguno | entrada diario Docker | ¿Sé explicar imagen/contenedor/puerto? |
| 2 | 90 min | Compose, redes, volúmenes | levantar compose simple | [[Docker_Compose]], [[Puertos_Volumenes_Redes]] | ninguno | `docker-compose.yml` anotado | ¿Sé por qué un servicio ve a otro por nombre? |
| 3 | 90 min | Diff/patch | crear y aplicar patch | [[Diff_y_Patch]], [[Git_Apply]] | ninguno | `changes.patch` | ¿Sé romper y arreglar un patch? |
| 4 | 90 min | Repos grandes | mapa de repo | [[Como_leer_un_repo_grande_sin_IA]], [[Mapa_de_un_repo]] | ninguno | `MAPA_REPO.md` | ¿Sé encontrar entrypoints y config? |
| 5 | 90 min | Requisitos/testing | dataset inicial | [[Testing_basado_en_requisitos]], [[Test_Cases]] | `coverage_checker.py` | coverage básico | ¿Sé explicar gap y trazabilidad? |
| 6 | 90 min | Golden set | etiquetas manuales | [[Golden_Set_para_evaluar_retrieval]] | `requirements_dataset.py` | CSVs revisados | ¿Hay relaciones correctas e incorrectas? |
| 7 | 90 min | Embeddings | similitud coseno | [[Embeddings_para_requisitos]], [[Similarity_Search]] | `embedding_thresholds.py` | top-k por requisito | ¿Veo FP/FN al cambiar threshold? |
| 8 | 90 min | BM25 | ranking lexical | [[BM25]] | `bm25_hybrid.py` | comparación BM25/dense | ¿Sé cuándo una sigla gana? |
| 9 | 90 min | Hybrid/RRF | combinar señales | [[Hybrid_Search]], [[RRF_Reranking]] | `bm25_hybrid.py` | tabla con alpha | ¿Sé defender un alpha inicial? |
| 10 | 90 min | Qdrant | colección y payload | [[Qdrant]], [[Qdrant_Filtros_Metadata]] | `qdrant_index_search.py` | colección `requirements` | ¿Sé filtrar por `module`? |
| 11 | 90 min | OpenWebUI | arquitectura | [[OpenWebUI_Arquitectura]], [[OpenWebUI_RAG]] | ninguno | diagrama propio | ¿Sé dónde entra Qdrant? |
| 12 | 90 min | Patch en contenedor | inspección | [[OpenWebUI_imagen_oficial_mas_patch]] | ninguno | checklist de comprobación | ¿Sé buscar `hybrid_search` dentro? |
| 13 | 90 min | Inferencia | vLLM/LiteLLM/Qwen | [[Motor_de_inferencia]], [[KV_Cache_Batching_Streaming]] | ninguno | curl preparado | ¿Sé qué componente optimiza tokens/s? |
| 14 | 90 min | Code embeddings | indexar funciones | [[Code_Embeddings]], [[Indexar_codigo_por_funciones_clases]] | `code_embedding_indexer.py` | búsquedas comparadas | ¿Sé cuándo usar `rg` primero? |
| 15 | 90 min | LangGraph/MCP | workflow | [[LangGraph]], [[MCP]] | ninguno | Mermaid del workflow | ¿Sé separar nodos, estado y herramientas? |
| 16 | 90 min | Atención | cross-attention A->B | [[Atencion_entre_dos_requisitos]] | `attention_requirements_from_scratch.py` | heatmaps | ¿Sé por qué A->B != B->A? |
| 17 | 90 min | Transformers reales | attentions BERT | [[Visualizar_matriz_de_atencion]] | `attention_requirements_with_transformers.py` | CSV + heatmap | ¿Sé por qué no es explicación causal? |
| 18 | 90 min | Wireshark/CAN | leer frames | [[Wireshark]], [[CAN]], [[Como_leer_paquetes]] | ninguno | tabla de campos | ¿Sé leer ID, DLC y payload? |
| 19 | 90 min | UDS/DoIP | diagnóstico | [[UDS]], [[DoIP]] | ninguno | chuleta de servicios | ¿Sé qué son DID y NRC? |
| 20 | 120 min | Autoencoders | anomalías CAN | [[Autoencoders_para_paquetes_CAN]], [[Features_para_CAN]] | `can_autoencoder.py` | métricas y threshold | ¿Sé explicar FP/FN del detector? |

## Lección guiada

Esta nota pertenece al plan de estudio. No la leas como una lista pasiva: conviértela en agenda.

### Preguntas

- ¿Qué bloque reduce más incertidumbre esta semana?
- ¿Qué entregable demostraría que lo entiendo?
- ¿Qué tema debo posponer aunque sea interesante?

### Evidencia de dominio

- [ ] Puedo explicar por qué este paso va antes que el siguiente.
- [ ] Tengo un entregable pequeño asociado.
- [ ] He marcado una duda para preguntar en la empresa.
